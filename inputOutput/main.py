from proses.proses import Proses

class Input(Proses):
    pastdata = [] #keperluan kata berulang
    outputData = [] #data yang akan dikeluarkan
    def __init__(self, input,jawaban:str) -> None:
        self.data = input #input yang dimasukkan
        self.Jawaban = jawaban.split() #jawaban dalam bentuk list
        for i in range(len(self.Jawaban)):
            self.outputData.append(" ") #akan menambahkan " " di setiap kata
        
    
                
        
        
    def __cekdata(self):
        """ 
        fungsi ini berfungsi untuk mengecek apakah data sudah dimasukkan atau belum
        Returns:
            1 jika belum dan 0 jika sudah
        """
        if self.data not in self.pastData:
            self.postData.append(self.data)
            return 1
        else:
            return 0
        
    def __cekJawaban(self, kalah, menang):
        """_summary_
        Args:
            kalah (function): fungsi untuk menampilkan jika kalah
            menang (function): fungsi untuk menampilkan jika menang

        Returns:
            program akan menengecek apakah jawaban benar atau salah, dan program akan mengecek apakah 
            program akan mengececek menang atau kalah
        """
        for i in range(len(self.Jawaban)):
            if self.data == self.Jawaban[i]:
                self.outputData[i] = self.data
        if " " not in self.outputData:
            return menang()
        else:
            return kalah()
            
        
        

        
    
            
    
    