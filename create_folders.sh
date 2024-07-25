#!/bin/bash

# Lista de matérias em inglês
subjects=(
    "Computer_Architecture"
    "Fundamentals_of_Computer_Networks"
    "Introduction_to_Computer_Programming"
    "Introduction_to_Information_Security"
    "Database"
    "Cloud_Computing"
    "Web_Development_in_HTML5_CSS_JavaScript"
    "Programming_Languages_Paradigms"
    "Computational_Thinking"
    "Rapid_Application_Development"
    "Data_Structures"
    "Mathematics_and_Logic"
    "Computer_Network_Protocols"
    "Information_Systems_and_Society"
    "Operating_Systems"
    "Data_Analysis"
    "Differential_and_Integral_Calculus"
    "Data_Science_in_Python"
    "Systems_Modeling_in_UML"
    "Basic_Software_Programming"
    "Algorithms_and_Complexity"
    "Multivariable_Calculus"
    "Software_Engineering"
    "Analytical_Geometry_and_Linear_Algebra"
    "Distributed_Systems_and_Parallel_Computing"
    "Graph_Algorithms"
    "Formal_Languages_and_Automata"
    "Quantitative_Methods"
    "Microcontroller_Programming"
    "Object_Oriented_Programming"
    "Cloud_IoT_and_Industry_4.0_Applications"
    "Artificial_Intelligence"
    "Mathematical_Modeling"
    "Software_Design_Patterns"
    "Mobile_Devices_Programming"
    "Image_Processing_Algorithms"
    "Compilers"
    "Cybersecurity"
    "Big_Data_Topics_in_Python"
)

# Criar pastas para cada matéria
for subject in "${subjects[@]}"; do
    mkdir -p "$subject"
done

echo "Folders created successfully."
