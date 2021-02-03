import torch
import torch.nn as nn

class attention(nn.Module):
    def __init__(self, Encoder, Decoder, input_size, hidden_size, output_size, dropout_p, n_layers = 2):
        super().__init__()
        self.input_size = input_size # input_size == embededing size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.encoder = Encoder(self.input_size, self.hidden_size, self.dropout_p, self.n_layers)
        self.decoder = Decoder(self.hidden_size, self.output_size, self.dropout_p, self.n_layers)

        self.softmax = nn.Softmax()

    def forward(self, data, encoder_outputs, decoder_hidden):
        assert data.shape[2] == self.input_size

        fir_hidden = self.encoder.return_f_hidden()
        fir_cell = self.encoder.return_f_cell()

        data_len = data.shape[2]
        output, (hidden, cell) = self.encoder(data, fir_hidden, fir_cell)

        # attn_score = torch.FloatTensor()

        # for i in range(len(encoder_outputs)):
        #     if i == 0:
        #         attn_score = attn_score.cat(torch.bmm(encoder_outputs[i], decoder_hidden))
        #     attn_score = torch.stack([attn_score, torch.bmm(encoder_outputs[i], decoder_hidden)])
        #     attn_score[i] = self.softmax(attn_score[i])

        


class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size, dropout_p, n_layers = 2):
        super().__init__()
        
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.embedding = nn.Embedding(input_size, hidden_size) # embedding_size == hidden_size
        self.lstm = nn.LSTM(
            input_size = input_size,
            output_size = hidden_size,
            batch_first = True,
            return_state = True,
            n_layers = n_layers,
            dropout = dropout_p,
            bidirectional = 2
        )

    def forward(self, input, hidden, cell):
        data = self.embedding(input)
        output, (hidden, cell) = self.lstm(data, (hidden, cell)).view(1,1,-1)
        return output, hidden, cell

    def return_f_hidden(self):
        return torch.zeros(1, 1, self.hidden_size) # lstm으로 각 state의 output을 얻을 수 없기 때문에 각 문장의 한 단어씩 lstm을 돌려 얻기 위해 (batch, seq_len, hidden_size)를 (1, 1, hidden_size)로 만들었다.

    def return_f_cell(self):
        return torch.zeros(1, 1, self.hidden_size)

class Decoder(nn.Module):
    def __init__(self, hidden_size, output_size, dropout_p, n_layers = 2):
        super().__init__()
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.embedding = nn.Embedding(output_size, hidden_size)
        self.lstm = nn.LSTM(
            input_size = hidden_size,
            output_size = output_size,
            dropout = dropout_p,
            batch_first = True,
            return_state = True,
            n_layers = n_layers
        )

        # self.softmax = nn.Softmax()  
    
    def forward(self, input, hidden, cell):
        data = self.embedding(input).view(1,1,-1)
        output, (hidden, cell) = self.lstm(data, (hidden, cell))
        
        return output, hidden, cell
