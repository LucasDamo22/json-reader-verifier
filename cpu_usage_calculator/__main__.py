from cpu_usage_calculator.cpu.cpu_class import Processor
import json
import glob

def main():

    paths = glob.glob('./cpu_usage_calculator/data/*.json')
    paths = sorted(paths)
    print(paths)
    for i in range(0, len(paths)):
        cpu1 = Processor()
        cpu2 = Processor() 
        print(f'for the file {paths[i]} this is the cpu distribution:')
        with open (paths[i], 'r') as raw:
            
            data = json.load(raw)
        
        tasks = data["Processos"].values()
        for value in tasks:
            if cpu1.get_coef()>cpu2.get_coef():
                cpu2.add_process(value[0]/value[1])
            else:
                cpu1.add_process(value[0]/value[1])
        print(f'cpu 1 = {cpu1.get_coef()}')
        print(f'cpu 2 = {cpu2.get_coef()}')
        print(f'==========')







if __name__ == "__main__":
    main()