# Employee management system.

## Code smells

- use enums when a variable can take one of a limited selection of values, in our case `role`.
- define custom exceptions to improve code readability and offer better debuging, like our `VacationDaysShortageError`, which accepts additional argument to better understand the cause of the exception once it is cought.
- use an `abstractmethod` for `pay` so that each employee based on payout can define their own `pay` method
