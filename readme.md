# Metaheuristic Optimization Assignment 2

### GSAT

Run the following command for the uf20-020 dataset

```
python main_gsat.py uf20-020.cnf
```

Run the following command for the uf20-021 dataset

```
python main_gsat.py uf20-021.cnf
```

You can also pass in an optional second argument to set the number of threads to use. By default this will be the number
of cpus you have. For example the below command will run 100 threads resulting in 100 results

```
python main_gsat.py uf20-020.cnf 100
```

### Novelty+


Run the following command for the uf20-020 dataset

```
python main_novelty_plus.py uf20-020.cnf
```

Run the following command for the uf20-021 dataset

```
python main_novelty_plus.py uf20-021.cnf
```

You can also pass in an optional second argument to set the number of threads to use. By default this will be the number
of cpus you have. For example the below command will run 100 threads resulting in 100 results

```
python main_novelty_plus.py uf20-020.cnf 100
```

The results of the experiment will be output to a csv file under ./experiments/novelty_plus


