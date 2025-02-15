# ft_package

A sample test package that provides simple list manipulation functions.

## Installation

You can install the package using pip:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

Here's how to use the functions provided by the package:

```python
from ft_package import count_in_list

# Example usage
result = count_in_list([1, 2, 3, 4, 5], 3)
print(result)  # Output: 1
```

## Functions

### `count_in_list(lst, item)`

Counts the number of occurrences of `item` in `lst`.

#### Parameters

- `lst`: List to search in
- `item`: Item to count in the list

#### Returns

- Number of occurrences of `item` in `lst`

### `ft_tqdm(lst)`

A simplified implementation of tqdm progress bar.

### Parameters

- `lst`: Range object to iterate over

### Returns

- None
