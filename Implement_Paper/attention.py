import torch
import torch.nn as nn

class attention(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, dropout_p):
        
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p

        self.lstm = nn.LSTM(
            input_size = input_size,
            hidden_size = hidden_size,
            batch_first = True,
            return_state = True,
            dropout = dropout_p
        )
    
    def forward(self, x, h_pre):
        pass

    def encoder(self, data):
        for t in range():
            pass

        
        
