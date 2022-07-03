
import wpf
from System.Windows import Application, window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication.xaml')

    def button_Click(self, sender, e):
        a = float(self.textBoxA.Text)
        b = float(self.textBoxB.Text)
        result = a + b
        self.labelResult.Content = str(result)


if __name__ == '__main__':
    Application().Run(MyWindow())