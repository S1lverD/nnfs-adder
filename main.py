from dataset import DataSet


class Neuron:

    def __init__(self, inputs, corect_result):
        self.inputs = inputs
        self.corect_result = corect_result
        self.height = 0.999999981270531
        self.last_error = 1
        self.smoothing = 0.000001
        self.correction = 0

    def calcul(self):
        return self.inputs[0] * self.height + self.inputs[1] * self.height

    def training(self):
        self.predict = self.inputs[0] * self.height + self.inputs[1] * self.height
        self.last_error = self.corect_result - self.predict
        self.correction = ( self.last_error / self.predict ) * self.smoothing
        self.height += self.correction



def main():
    i = 0
    ds = DataSet("dataset.db")
    unit = ds.read_from_dataset()[0]
    neuron = Neuron(unit[:2], unit[2])

    # print(unit)
    # print(neuron.calcul())
    while neuron.last_error > 0.000001:
        i += 1
        neuron.training()
        if (i % 100000 == 0):
            print("Iteration number:", i, "\tError :", neuron.last_error, "\tPredition :", neuron.predict)
    

    print("Corect result :", unit[2])
    print("Calculated height :", neuron.height)



if __name__ == "__main__":
    main()
