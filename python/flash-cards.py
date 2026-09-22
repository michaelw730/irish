import duckdb

FILE_CONV = "../vocab_conv.csv"
con = duckdb.connect()

def load_csv():
    con.execute(f"CREATE TABLE vocab AS SELECT * FROM read_csv_auto('{FILE_CONV}', delim='\t');")

def main(response, program, episode):
    cursor = con.execute("SELECT * FROM vocab WHERE program = ? AND episode = ?", (program, episode))
    columns = [desc[0] for desc in cursor.description]

    all_rows = cursor.fetchall()

    for row in all_rows:
        if row is None:
            continue
        row_as_dict = dict(zip(columns, row))

        # clean up None values
        for key in row_as_dict:
            if row_as_dict[key] is None:
                row_as_dict[key] = ""

        # skip template rows
        if row_as_dict['type'] == "TEMPLATE":
            continue

        if response == "1":
            question = f"Q: {row_as_dict['irish']} [S/P: {row_as_dict['s_p']}] (INFO: {row_as_dict['info']})"
            answer = f"A: {row_as_dict['meaning']} (IRISH_PHONETIC: {row_as_dict['phonetic']})"
        else:
            question = f"Q: {row_as_dict['meaning']} [S/P: {row_as_dict['s_p']}] (INFO: {row_as_dict['info']})"
            answer = f"A: {row_as_dict['irish']} (IRISH_PHONETIC: {row_as_dict['phonetic']})"

        print(question, end="")
        input()
        # input("Press Enter to see the answer...")
        print(answer, end="\t\t")
        #input()
        input("Press Enter to see the next question...")
        print()

if __name__ == "__main__":
    load_csv()

    print("Press Enter 1 for Irish questions, or Enter 2 for English questions...")

    response = 0
    response_options = ["1", "2"]
    while response not in response_options:
        response = input()

        if response not in response_options:
            print("Invalid input. Please enter 1 or 2.")

    print(f"Please enter the program")
    program = input()

    print(f"Please enter the episode number")
    episode = input()

    print("\nStarting flash cards...\n")
    main(response, program, episode)
