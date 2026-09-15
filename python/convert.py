import duckdb

FILE = "../vocab.csv"
FILE_CONV = "../vocab_conv.csv"
FILE_MD = "../vocab.md"

def main_csv():
    con = duckdb.connect()
    con.execute(f"CREATE TABLE vocab AS SELECT * FROM read_csv_auto('{FILE}', delim='\t',sample_size = -1, ignore_errors = false);")
    cursor = con.execute("SELECT * FROM vocab")

    # Extract column names using a list comprehension
    columns = [desc[0] for desc in cursor.description]
    print(f"Column names: {columns}")

    # Print the header
    output = ""
    delim = "\t"

    header = ""
    header += f"{delim}".join(columns) + "\n"

    all_rows = cursor.fetchall()

    for row in all_rows:
        if row is None:
            break
        print(f"Row: {row}")
        row_as_dict = dict(zip(columns, row))
        #print(row)

        row = ('' if item is None else item for item in row)
        # # not dynamic
        # if "$" not in row_as_dict['irish']:
        output += f"{delim}".join(map(str, row)) +"\n"

        # dynamic
        if "$" in row_as_dict['irish']:
            # clean up None values
            for key in row_as_dict:
                if row_as_dict[key] is None:
                    row_as_dict[key] = ""

            # find dynamic word
            words = row_as_dict['irish'].split(" ")
            for word in words:
                i = 0
                if "$" in word:
                    print(f"Found a word with $: {word}")
                    break

            group = word.replace("$", "").strip()
            group = group.replace("?", "")
            group = group.replace(".", "")

            sql = f"SELECT irish, meaning, phonetic FROM vocab WHERE \"group\" = '{group}'"
            cursor = con.sql(sql)
            dynamic_words = cursor.fetchall()


            if len(dynamic_words) > 0:
                for dynamic_irish, dynamic_meaning, dynamic_phonetic in dynamic_words:
                    if dynamic_phonetic is None:
                        dynamic_phonetic = ""
                    output += f"{row_as_dict['program']}{delim}"
                    output += f"{row_as_dict['episode']}{delim}"
                    output += f"{row_as_dict['topic']}{delim}"
                    output += f"{row_as_dict['topic2']}{delim}DYNAMIC{delim}"
                    output += f"{row_as_dict['group']}{delim}"
                    output += f"{row_as_dict['irish'].replace(group, dynamic_irish).replace('$', '')}{delim}"
                    output += f"{row_as_dict['meaning'].replace(group, dynamic_meaning).replace('$', '')}{delim}"
                    output += f"{row_as_dict['practice_ideas']}{delim}"
                    output += f"{row_as_dict['s_p']}{delim}"
                    output += f"{row_as_dict['m_f']}{delim}"
                    output += f"{row_as_dict['literal_meaning'].replace(group, dynamic_meaning).replace('$', '')}{delim}"
                    output += f"{row_as_dict['phonetic'].replace(group, dynamic_phonetic).replace('$', '')}{delim}"
                    output += f"{row_as_dict['sound']}{delim}"
                    output += f"{row_as_dict['info']}\n"

    # Optionally, write the output to a file
    with open(FILE_CONV, "w") as f:
        f.write(header)
        f.write(output)

def main_duckdb():
    con = duckdb.connect()
    con.execute(f"CREATE TABLE vocab AS SELECT * FROM read_csv_auto('{FILE_CONV}', delim='\t');")
    cursor = con.sql("SELECT * FROM vocab")

    # Extract column names using a list comprehension
    columns = [desc[0] for desc in cursor.description]
    print(f"Column names: {columns}")

    # Print the header
    output = ""

    header = ""
    header += "| " + " | ".join(columns) + " |\n"
    header += "|" + "---|" * len(columns) + "\n"

    # Print the data rows
    topic = ""
    topic_old = ""
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        row_as_dict = dict(zip(columns, row))
        print(row)

        topic = row_as_dict['program'] + " - " + row_as_dict['topic']
        if topic != topic_old:
            output += f"\n## {topic}\n\n"
            output += header
        row = ('' if item is None else item for item in row)
        output += "| " + " | ".join(map(str, row)) + " |\n"

        topic_old = topic

    # Optionally, write the output to a file
    with open(FILE_MD, "w") as f:
        f.write(output)

if __name__ == "__main__":
    main_csv()
    main_duckdb()
