class Loader(object):
    """
    interface for data loader wrappers
    """
    def load_data(self, file_name):
        """
        loads the data into memory
        :param file_name: name of the file to load
        :return: pandas object
        """
        raise NotImplementedError
