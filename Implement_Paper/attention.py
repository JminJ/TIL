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

        self.encoder_hidden = self.encoder.return_output_list()

    def forward(self, data):
        

class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size, dropout_p, n_layers = 2):
        super().__init__()
        self.input_size = input_size # input_size == embededing size
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.en_output_list = []

        self.lstm = nn.LSTM(
            input_size = input_size,
            output_size = hidden_size,
            batch_first = True,
            return_state = True,
            n_layers = n_layers,
            dropout = dropout_p
        )

    def forward(self, data):
        output, (hidden, cell) = self.lstm(data)
        self.en_output_list.append(output) 

        return hidden, cell

    def return_output_list(self):
        return self.en_output_list

class Decoder(nn.Module):
    def __init__(self, hidden_dize, output_size, dropout_p, n_layers = 2):
        super().__init__()
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.lstm = nn.LSTM(
            input_size = hidden_size,
            output_size = output_size,
            dropout = dropout_p,
            batch_first = True,
            return_state = True,
            n_layers = n_layers
        )

        self.softmax = nn.Softmax()  
        

    def forward(self, input, hidden, cell):
        output, (hidden, cell) = self.lstm(input, (hidden, cell))
        
        return output
