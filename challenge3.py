def solution(N):
    num_occurrences = N // 26
    remainder = N % 26
    result = ""
    for i in range(26):
        char = chr(ord('a') + i)
        if i < remainder:
            result += char * (num_occurrences + 1)
        else:
            result += char * num_occurrences
    return result

def main():
    N = int(input("Enter the length of the string (N): "))
    
    result = solution(N)
    
    print("Generated string:", result)

if __name__ == "__main__":
    main()
