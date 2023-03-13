# JSON Reader and Verifier
- This project its the migration of the YAML Reader and Verifier to python, and to JSON files. This is the older project: https://github.com/LucasDamo22/yaml-reader-verifier

- This project contains two programs. A cpu usage calculator for real-time systems, and a tester for this program. The calculator reads a JSON file that contains de minimal processing time, and the maximal processing time possible.

## How to use the random_task_generator module:
- From the root folder, invoke the module with "python3 -m random_task_generator xx yy" passing two arguments on the xx and yy. These values should be the respectively the minimal (xx) amount of processing power targeted,  and the maximal (yy). The module will generate a range of json files directly on the "data" folder on the calculator module, that has a set of tasks that sum up to the targeted processing usage.

## How to use the random_task_generator module:
- From the root folder invoke the module with "python3 -m cpu_usage_calculator" with no arguments. It will access ALL .json files on the "data" folder an process its tasks

Beware that all files that terminate on ".json" will be acessed by the program , and if hey do not follow the pattern shown in the example.yaml on the root folder, the program will not work correctly.

## Built and tested on CentOs 7

# Runtime requirements:
- python3