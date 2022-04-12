class PoolEmptyException(Exception):
    def __str__(self):
        """
        proxypool-fix is used out
        :return:
        """
        return repr('no proxy in proxypool-fix')
