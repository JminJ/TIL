import torch
import torch.nn as nn

class attention(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, dropout_p):
        
        self.input_size = input_size # input_size == embededing size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

        self.en_output_list = []

        self.en_lstm = nn.LSTM(
            input_size = input_size,
            hidden_size = hidden_size,
            batch_first = True,
            return_state = True,
            n_layers = self.n_layers,
            dropout = dropout_p
        )
        self.de_lstm = nn.LSTM(
            input_size = input_size,
            hidden_size = hidden_size,
            batch_first = True,
            return_state = True,
            n_layers = self.n_layers,
            dropout = dropout_p
        )
    
    def forward(self, x, h_pre):
        pass

class Encoder(nn.Module):
    def __init__(self, input_size, hidden_size, dropout_p, n_layers = 2):
        self.input_size = input_size # input_size == embededing size
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.n_layers = n_layers

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

class Decoder(nn.Module):
    def __init__(self, hidden_dize, output_size, dropout_p,n_layers = 2):
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
        
        
        
