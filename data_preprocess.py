

if __name__ == "__main__":
    with open("data/jinrong.nt") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            print(line.split())