import torch 
import torch.nn as nn 
import torch.optim as optim 

class SimpleNN(nn.Module): 

    def __init__(self): 

        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2,5) 
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5,1)
    
    def forward(self, x): 

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x



model = SimpleNN()
print(model) 
