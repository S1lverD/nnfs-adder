from dataset import DataSet


class Neuron:

    def __init__(self, inputs, corect_result):
        self.inputs = inputs
        self.corect_result = corect_result
        self.height = 0.005
        self.last_error = 0
        self.smoothing = 0.0000001
        self.correction = 0

    def calcul(self):
        return self.inputs[0] * self.height + self.inputs[1] * self.height

    def training(self):
        self.predict = self.inputs[0] * self.height + self.inputs[1] * self.height
        self.last_error = ( self.corect_result - self.predict ) * self.smoothing
        self.correction = self.last_error / self.predict
        self.height += self.correction


def main():
    ds = DataSet("dataset.db")
    unit = ds.read_from_dataset()[0]

    print("For A =", unit[0], "and B =", unit[1], "result is", unit[2])

    neuron = Neuron(unit[:2], unit[2])
    print(">", neuron.calcul())

    
main()