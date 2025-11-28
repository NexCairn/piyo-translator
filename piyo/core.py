class PiyoTranslator:
    """
    Translates text to Piyo language and back.
    Uses UTF-8 binary encoding mapped to 'ピ' (0) and 'ヨ' (1).
    """

    ZERO_CHAR = "ピ"
    ONE_CHAR = "ヨ"

    @classmethod
    def encode(cls, text: str) -> str:
        """
        Encodes a string into Piyo language.
        """
        if not text:
            return ""
        
        # Convert string to bytes (UTF-8)
        bytes_data = text.encode('utf-8')
        
        # Convert bytes to binary string
        binary_string = ''.join(format(byte, '08b') for byte in bytes_data)
        
        # Map 0 -> ピ, 1 -> ヨ
        piyo_text = binary_string.replace('0', cls.ZERO_CHAR).replace('1', cls.ONE_CHAR)
        
        return piyo_text

    @classmethod
    def decode(cls, piyo_text: str) -> str:
        """
        Decodes Piyo language back into a string.
        """
        if not piyo_text:
            return ""

        # Validate input (allow whitespace but ignore it for decoding if we want strictness, 
        # but for now let's assume strict input or strip whitespace)
        # For robustness, let's strip whitespace
        clean_text = piyo_text.replace(" ", "").replace("\n", "").replace("\t", "")
        
        # Map ピ -> 0, ヨ -> 1
        binary_string = clean_text.replace(cls.ZERO_CHAR, '0').replace(cls.ONE_CHAR, '1')
        
        # Validate that we only have 0s and 1s
        if not all(c in '01' for c in binary_string):
             raise ValueError("Input contains invalid characters. Only 'ピ' and 'ヨ' are allowed.")

        # Split into 8-bit chunks
        if len(binary_string) % 8 != 0:
            raise ValueError("Invalid Piyo string length. Must be a multiple of 8 bits.")
            
        bytes_list = []
        for i in range(0, len(binary_string), 8):
            byte_str = binary_string[i:i+8]
            bytes_list.append(int(byte_str, 2))
            
        # Convert back to bytes
        bytes_data = bytes(bytes_list)
        
        # Decode UTF-8
        return bytes_data.decode('utf-8')
