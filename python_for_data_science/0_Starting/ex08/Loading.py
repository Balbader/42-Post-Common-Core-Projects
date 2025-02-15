def ft_tqdm(lst: range) -> None:
    """
    A simplified implementation of tqdm progress bar.
    Args:
        lst (range): Range object to iterate over
    Yields:
        Elements from the input range while displaying a progress bar
    """

    total = len(lst)
    bar_length = 60  # Length of progress bar

    for i, item in enumerate(lst, 1):
        percentage = (i / total) * 100
        filled_length = int(bar_length * i // total)
        bar = '=' * (filled_length - 1) + '>' + ' ' \
            * (bar_length - filled_length)

        # Create progress bar string
        progress_bar = f"\r{percentage:3.0f}%|[{bar}]| {i}/{total}"

        # Print progress bar
        print(progress_bar, end='', flush=True)

        yield item
