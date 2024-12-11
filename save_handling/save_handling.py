import pickle
import os

class SaveLoadSystem:
    def __init__(self, file_extension, save_folder):
        self.file_extension = file_extension
        self.save_folder = save_folder

    def save_data(self, data, name):
        self.create_folder(name)
        data_file = open(os.path.join(self.save_folder, name + "." + self.file_extension), "wb+")
        pickle.dump(data, data_file)

    def load_data(self, name):
        data_file = open(os.path.join(self.save_folder, name + "." + self.file_extension), "rb")
        data = pickle.load(data_file)
        return data

    def create_folder(self, name):
        if not os.path.exists(os.path.join(self.save_folder)):
            os.makedirs(os.path.join(self.save_folder))

    def check_for_file(self, name):
        return os.path.exists(os.path.join(self.save_folder, name + "." + self.file_extension))