import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import time
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import re
plt.switch_backend('agg')

SOS_token = 0
EOS_token = 1
device = torch.device('cpu')

class Lang:
    def ___init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {0: 'SOS', 1: 'EOS'}
        self.n_words = 2 # SOS, EOS 포함
    
    def addSentence(self, sentnece):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.wrod2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NDF', s)
        if unicodedata.category(c) != 'Mn'
    )


def normalizeString(s):
    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r"\1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s


def readLangs(lang1, lang2, reverse=False):
    print("Reading lines...")

    # 파일을 읽고 줄로 분리
    lines = open('data/%s-%s.txt' % (lang1, lang2), encoding='utf-8').\
        read().strip().split('\n')

    # 모든 줄을 쌍으로 분리하고 정규화
    pairs = [[normalizeString(s) for s in l.split('\t')] for l in lines]

    # 쌍을 뒤집고, Lang 인스턴스 생성
    if reverse:
        pairs = [list(reversed(p)) for p in pairs]
        input_lang = Lang(lang2)
        output_lang = Lang(lang1)
    else:
        input_lang = Lang(lang1)
        output_lang = Lang(lang2)

    return input_lang, output_lang, pairs


eng_prefixes = (
    "i am ", "i m ",
    "he is", "he s ",
    "she is", "she s ",
    "you are", "you re ",
    "we are", "we re ",
    "they are", "they re "
)


def filterPair(p):
    return len(p[0].split(' ')) < MAX_LENGTH and \
        len(p[1].split(' ')) < MAX_LENGTH and \
        p[1].startswith(eng_prefixes)


def filterPairs(pairs):
    return [pair for pair in pairs if filterPair(pair)]

def prepareData(lang1, lang2, reverse=False):
    input_lang, output_lang, pairs = readLangs(lang1, lang2, reverse)
    print("Read %s sentence pairs" % len(pairs))
    pairs = filterPairs(pairs)
    print("Trimmed to %s sentence pairs" % len(pairs))
    print("Counting words...")
    for pair in pairs:
        input_lang.addSentence(pair[0])
        output_lang.addSentence(pair[1])
    print("Counted words:")
    print(input_lang.name, input_lang.n_words)
    print(output_lang.name, output_lang.n_words)
    return input_lang, output_lang, pairs


input_lang, output_lang, pairs = prepareData('eng', 'fra', True)
print(random.choice(pairs))


class attention(nn.Module):
    def __init__(self, Encoder, Decoder, input_size, hidden_size, output_size, dropout_p, n_layers = 2):
        super().__init__()
        self.input_size = input_size # input_size == vocab size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.dropout_p = nn.Dropout(dropout_p)
        self.n_layers = n_layers

        self.attn_combine = nn.Linear(self.hidden_size * 2, self.hidden_size)

        self.embedding = nn.Embedding(input_size, hidden_size)

        self.softmax = nn.Softmax()

    def forward(self, input, hidden, encoder_outputs):
        embd_data = self.embedding(input)
        embd_data = self.dropout_p(embd_data)

        attn_weights = self.softmax(torch.cat((embd_data[0], hidden[0]), 1), dim = 1)

        attn_applied = torch.bmm(attn_weights.unsqueeze(0), encoder_outputs.unsqueeze(0))
        output = torch.cat((embd_data[0], attn_applied[0]), 1)
        output = self.attn_combine(output).unsqueze(0)

        output = F.relu(output) # output shape == relu의 input shape

        return output, hidden, attn_weights


class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size, dropout_p, n_layers = 2):
        super().__init__()
        
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.embedding = nn.Embedding(input_size, hidden_size) # embedding_size == hidden_size

        self.gru = nn.GRU(
            input_size = input_size,
            hidden_size = hidden_size,
            batch_first = True,
            return_state = True,
            n_layers = n_layers,
            dropout = dropout_p,
            bidirectional = 2
        )

    def forward(self, input, hidden, cell):
        embd_data = self.embedding(input)
        output, hidden = self.gru(embd_data, hidden).view(1,1,-1)
        return output, hidden

    def return_f_hidden(self):
        return torch.zeros(1, 1, self.hidden_size) # gru로 각 state의 output을 얻을 수 없기 때문에 각 문장의 한 단어씩 gru을 돌려 얻기 위해 (batch, seq_len, hidden_size)를 (1, 1, hidden_size)로 만들었다.


class Decoder(nn.Module):
    def __init__(self, hidden_size, output_size, dropout_p, n_layers = 2):
        super().__init__()
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.l_softmax = F.log_softmax()

        self.out = nn.Linear(hidden_size, output_size)

        self.gru = nn.GRU(
            input_size = hidden_size,
            hidden_size = output_size,
            dropout = dropout_p,
            batch_first = True,
            return_state = True,
            n_layers = n_layers
        )
    
    def forward(self, input, hidden, attn_weights): # input : attention의 output
        output, hidden = self.gru(input, hidden)
        
        output = self.l_softmax(self.out(output[0]), dim = 1)

        return output, hidden, attn_weights


MAX_LENGTH = 10

teacher_forcing_ratio = 0.5

def train(input_tensor, target_tensor, encoder, decoder, attention, encoder_optimizer, decoder_optimizer, attention_optimizer, criterion, max_length = MAX_LENGTH):
    encoder_hidden = encoder.return_fir_hidden()
    encoder_cell = encoder.return_fir_cell()

    encoder_optimizer.zero_grad()
    decoder_optimizer.zero_grad()

    input_length = input_tensor.size(0)
    target_length = target_tensor.size(0)

    encoder_outputs = torch.zeros(max_length, encoder.hidden_size)
    
    loss = 0

    for i in range(input_length):
        encoder_output, encoder_hidden = encoder(input_tensor[i], encoder_hidden)
        encoder_outputs[i] = encoder_output[0][0]
    
    decoder_input = torch.tensor([[SOS_token]], device = device)

    decoder_hidden = encoder_hidden

    use_teacher_forcing = True if random.random() < teacher_forcing_ratio else False

    if use_teacher_forcing:
        for i in range(target_length):
            decoder_output, decoder_hidden, decoder_attn = attention(decoder_input, decoder_hidden, encoder_outputs)
            decoder_output, decoder_hidden, decoder_attn = decoder(decoder_output, decodder_hidden, decoder_attn)

            loss += criterion(decoder_output, target_tensor[i])
            decoder_input = target_tensor[i]
    
    else:
        for i in range(target_length):
            decoder_output, decoder_hidden, decoder_attn = attention(decoder_input, decoder_hidden, encoder_outputs)
            decoder_output, decoder_hidden, decoder_attn = decoder(decoder_output, decodder_hidden, decoder_attn)

            topv, topi = decoder_output.topk(1)
            decoder_input = topi.squeeze().detach()

            loss += criterion(decoder_output, target_tensor[i])
            if decoder_input.item() == EOS_token:
                break
    
    loss.backward()

    encoder_optimizer.step()
    decoder_optimizer.step()

    return loss.item() / target_length


# 학습 데이터 준비 : indexesFromSentence ~ tensorsFromPair
def indexesFromSentence(lang, sentence):
    return [lang.word2index[word] for word in sentence.split(' ')] # 띄어쓰기 단위로 문장 내 단어를 split(영어 용도) 한 뒤, index로 변환

def tensorFromSentence(lang, sentence):
    indexes = indexesFromSentence(lang, sentence)
    indexes.append(EOS_token)

    return torch.tensor(indexes, dtype = torch.lang).view(-1, 1)

def tensorsFromPair(pair):
    input_tensor = tensorFromSentence(input_lang, pair[0])
    target_tensor = tensorFromSentence(output_lang, pair[0])

    return (input_tensor, target_tensor)


# 헬퍼 함수 : asMinutes, timeSince
def asMinutes(s):
    m = math.floor(s / 60)
    s -= m * 60

    return '%dm %ds' % (m, s)

def timeSince(since, percent):
    now = time.time()
    s = now - since
    es = s / (persent)
    rs = es - s

    return '%s (- %s)' % (asMinutes(s, asMinutes(rs)))

def showPlot(points): # points == trainIter의 plot_losses
    plt.pigure()
    fig, ax = plt.subplots()
    # 주기적인 간격에 이 locator가 tick을 설정한다.
    loc = ticker.MultipleLocator(base=0.2)
    ax.yaxis.set_major_locator(loc)
    plt.plot(points)


# train 함수를 돌려주는 함수, 상태 표기 및 그래프를 그린다.
def trainIters(encoder, decoder, attention, n_iters, print_every = 1000, plot_every = 100, learning_rate = 0.01):
    # 시작 시간 count
    start = time.time()
    plot_losses = []
    print_loss_total = 0 # print_every 마다 초기화
    plot_loss_total = 0 # plot_every 마다 초기화

    encoder_optimizer = optim.SGD(encoder.parameters(), lr = learning_rate)
    decoder_optimizer = optim.SGD(decoder.parameters(), lr = learning_rate)
    attention_optimizer = optim.SGD(attention.parameters(), lr = learning_rate)
    training_parirs = [tensorsFromPair(random.choice(pairs)) for i in range(n_iters)]
    criterion = nn.NLLoss()

    for iter in range(1, n_iters+1):
        training_pair = training_parirs[iter-1]
        input_tensor = training_pair[0]
        target_pair = training_pair[0]

        loss = train(input_tensor, target_tensor, encoder, decoder, attention, encoder_optimizer, decoder_optimizer, attention_optimizer, criterion)
        print_loss_total += loss
        plot_loss_total += loss

        if iter % print_every == 0:
            print_loss_avg = print_loss_total / print_every
            print_loss_total = 0
            print('%S (%D %D%%) %.4F' % (timeSince(start, iter / n_iters), iter, iter / n_iters * 100, print_loss_avg))

        if iter % plot_every == 0:
            plot_loss_avg = plot_loss_total / plot_every
            plot_losses.append(plot_loss_avg)
            plot_loss_total = 0

    showPlot(plot_losses)

def evaluate(encoder, decoder, attention, sentence, max_length = MAX_LENGTH):
    with torch.no_grad():
        input_tensor = tensorFromSentence(input_lang, sentence)
        input_length = input_tensor.size()[0]
        encoder_hidden = encoder.return_f_hidden()

        encoder_outputs = torch.zeros(max_length, encoder.hidden_size)
        
        for i in range(input_length):
            encoder_output, encoder_hidden = encoder(input_tensor[i], encoder_hidden)
            encoder_outputs[i] += encoder_output[0, 0]

        decoder_input = torch.tensor([[SOS_token]], device = device)
        
        decoder_hidden = encoder_hidden

        decoded_words = []
        decoder_attentions = torch.zeros(max_length, max_length)

        for i in range(max_length):
            decoder_output, decoder_hidden, decoder_attention = decoder(decoder_input, decoder_hidden, encoder_outputs)
            decoder_attentions[i] = decoder_attention.data
            topv, topi = decoder_output.data.topk(1)
            if topi.item() == EOS_token: # torch.Tensor.item() : 한 값을 포함하고 있는 tensor로 부터 Python number를 가져온다.
                decoded_words.append('<EOS>')
                break
            else:
                decoded_words.append(output_lang.index2word[topi.item()])

            decoder_input = topi.squeeze().detach()

        return decoded_words, decoder_attentions[:i + 1]


def evaluateRandomly(encoder, decoder, n = 10):
    for i in range(n):
        pair = random.choice(pairs)
        print('>', pairs[0])
        print('=', pair[1])
        output_words, attentions = evaluate(encoder, decoder, pair[0])
        output_sentence = ' '.join(output_words)
        print('<', output_sentence)
        print('')