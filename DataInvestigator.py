class DataInvestigator:
    def __init__(self, file_csv):
        self.df = file_csv

    def baseline(self, col):
        try:
            mode = self.df.iloc[:, col].mode()
            return mode.iloc[0] if not mode.empty else None
        except Exception:
            return None

    def corr(self, col1, col2):
        try:
            return self.df.iloc[:, col1].corr(self.df.iloc[:, col2])
        except Exception:
            return None

    def zeroR(self, col):
        return self.baseline(col)
