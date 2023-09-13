class Tomark:

    @staticmethod
    def table(list_of_dicts):
        """Convert a list of dictionaries into a Markdown table.

        list_of_dicts -- A list of dictionaries, each dict is a row
        """
        if not list_of_dicts:
            return ""

        # Extract keys from the first dictionary
        keys = list(list_of_dicts[0].keys())

        # Create the header row and separator
        markdown_header = "| " + " | ".join(keys) + " |\n"
        markdown_separator = "| " + " | ".join(["---"] * len(keys)) + " |\n"

        # Convert the list of dictionaries into a Markdown table
        markdown_table = [markdown_header, markdown_separator]

        for row in list_of_dicts:
            markdown_row = "| " + " | ".join(str(row.get(key, "")) for key in keys) + " |\n"
            markdown_table.append(markdown_row)

        return "".join(markdown_table)
