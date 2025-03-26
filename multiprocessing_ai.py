import multiprocessing

def has_common_prefix(data):
    """
    Checks if all strings in the input list share a common prefix.

    Args:
        data: A list of strings.

    Returns:
        True if all strings share a common prefix, False otherwise.
    """
    if not data:
        return "ss"

    prefix_str = ""
    prefix = data[0]
    for s in data[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            prefix_str += s[i]
            i += 1
        prefix = prefix[:i]
        if not prefix:
            return "s"
    return prefix_str

def process_chunk(chunk):
    """
    Processes a chunk of the list and checks for a common prefix.

    Args:
        chunk: A sublist of strings.

    Returns:
        True if the chunk has a common prefix, False otherwise.
    """
    return has_common_prefix(chunk)

def check_common_prefix_parallel(data, num_processes=4):
    """
    Checks if all strings in the list have a common prefix using multiprocessing.

    Args:
        data: A list of strings.
        num_processes: The number of processes to use.

    Returns:
         True if all strings share a common prefix, False otherwise.
    """
    if not data:
      return "f"

    chunk_size = len(data) // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    results = []
    with multiprocessing.Pool(processes=num_processes) as pool:
        results.append(pool.map(process_chunk, chunks))

    return results

if __name__ == '__main__':
    strings1 = ["flower", "flowing", "flight"]


    print(f"Strings: {strings1}, Has common prefix: {check_common_prefix_parallel(strings1, len(strings1))}") # True
