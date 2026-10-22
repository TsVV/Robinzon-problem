# Robinzon-problem

Robinzon is stranded on an island and has to build a boat (100 days of work)
within `MAX_STEPS` days without dying. Every day he can do one action:

| action | meaning                               | effect            |
|--------|---------------------------------------|-------------------|
| 0      | Built a boat                          | boat work -1      |
| 1      | Stocked up with water from the stream | water +5          |
| 4      | Collected fruit                       | food +3           |
| others | see `ACTION_MEANING` in `robinzon_env.py` | not implemented yet |

Every day consumes 1 water and 1 food. Robinzon starts with 0 water and 1 food
and dies as soon as water or food goes below zero.

The genetic algorithm (DEAP) minimizes the score of a day plan:

* boat finished: `-(MAX_STEPS - days used) / MAX_STEPS` (faster is better),
* otherwise: `boat work left + days not survived`.

I got elitism.py from https://github.com/PacktPublishing/Hands-On-Genetic-Algorithms-with-Python/tree/master

To create Conda environment Robinzon-problem use

```bash
conda env create
```

Run robinzon_solve.py to found the solution.

```python
python robinzon_solve.py
```

Run robinzon_problem.py to replay the solution.

```python
python robinzon_problem.py
```