class Solution:
    """
    Python中可以通过以"0b"或者"-0b"开头的字符串来表示二进制，如下所示
    0b101 # 输出5
    0b10  # 输出2
    0b111 # 输出7
    -0b101 # 输出-5
    """
    def encode(self, num: int) -> str:
        # bin return the binary format number
        return bin(num + 1)[3:]
