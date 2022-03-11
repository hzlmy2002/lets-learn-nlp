import sys, os

class Checker:

    def __init__(self):
        self.success = True
    
    def run(self):
        self.check_deps()
        self.check_model()
        if self.success:
            print("\nOverall: Success! You're good to go!")
        else:
            print("\nOverall: Failure, check the cells below to resolve issues and try again")

    def check_deps(self):

        def get_data_from_file(filename):
            f = open(filename, "r")
            d = f.readlines()
            f.close()
            return d

        f1, f2 = sys.argv[1], sys.argv[2]
        missing = []
        data_1 = get_data_from_file(f1)
        data_2 = get_data_from_file(f2)
        os.remove(f2) # remove the copied requirements file
        for line in data_1:
            if line not in data_2:
                missing.append(line)
        missing_deps = ",".join(missing).strip()
        if len(missing) > 0:
            print(f"Test (1/2): Failed (dependencies missing: {missing_deps})")
            self.success = False
        else:
            print(f"Test (1/2): Passed")

    def check_model(self):
        try:
            import spacy
            spacy.load("en_core_web_md")
            print(f"Test (2/2): Passed")
        except Exception as e:
            print(f"Test (2/2): Failed\nCould not load language model: {e}")
            self.success = False



if __name__ == "__main__":
    Checker().run()
    
