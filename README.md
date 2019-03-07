## Bestoon python client
A simple python client for [Bestoon Project](https://github.com/jadijadi/bestoon)

### How to run

1. Install `python` in your system.
2. Clone the project using: `git clone https://github.com/Nimaebrazeh/bestoon-python-client`.
3. Install requirements package using `pip install -r requirements.txt`

## Usage

You can set your API token key first with instance of client:

```python
bestoon = Bestoon(YOUR-TOKEN) # make an Bestoon object and set API token to YOUR-TOKEN
```
If you forgot API token key, use `login()` method instead of above way (This method returns your API token):

```python
bestoon = Bestoon() # make an Bestoon object
bestoon.login(YOUR-USERNAME, YOUR-PASSWORD) # return API token
bestoon.set_token(YOUR-TOKEN) # set API token to YOUR-TOKEN
```

### Set expense
Set your expense with `amount` and `text` in arguments

```python
bestoon.set_expense('30000', 'Test')
```

### Set income
Set your income with `amount` and `text` in arguments

```python
bestoon.set_income('50000', 'Test')
```

### Get expenses
Get your expenses with `number(optional)` in arguments
```python
bestoon.get_expenses() # return all expenses as json format
bestoon.get_expenses(5) # return last 5 expenses as json format
```

### Get incomes
Get your incomes with `number(optional)` in arguments
```python
bestoon.get_incomes() # return all incomes as json format
bestoon.get_incomes(5) # return last 5 incomes as json format
```

### Get general status
You can manage your general status of expenses and incomes.
```python
bestoon.get_general_status() # return amount count and amount sum of all incomes and expenses
```

## TODO
- [ ] add fromdate and todate arguments to get_general_status() method
- [ ] export data to csv 
- [ ] export data to chart 

### License
The MIT License (MIT). Please see [License File](LICENSE) for more information.

