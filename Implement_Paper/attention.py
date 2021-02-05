import torch
import torch.nn as nn
import torch.nn.functional as F

class attention(nn.Module):
    def __init__(self, Encoder, Decoder, input_size, hidden_size, output_size, dropout_p, n_layers = 2):
        super().__init__()
        self.input_size = input_size # input_size == embededing size
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

    def return_f_cell(self):
        return torch.zeros(1, 1, self.hidden_size)


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

def train(input_tensor, target_tensor, encoder, decoder, attention, encoder_optimizer, decoder_optimizer, criterion, max_length = MAX_LENGTH):
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
    
    decoder_input = torch.tensor([[SOS_token]])

    decoder_hidden = encoder_hidden

    use_teacher_forcing = True if random.random() < teacher_forcing_ratio else False

    if use_teacher_forcing:
        for i in range(target_length):
            pass