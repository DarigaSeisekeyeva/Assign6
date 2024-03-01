from rent_service import rentService


def main():
    rent_service = rentService()
    rent_service.access()


    while True:

        rent_service.run()
        command = input("Enter command (clean to clean the database, q to quit): ")
        if command.lower() == 'clean':
            rent_service.clean_database()
        elif command.lower() == 'q':
            break

        elif command.lower() == 'backup_json':
            filename = input("Enter filename for backup JSON: ")
            rent_service.save_to_backup_json(filename)
            print(f"Backup saved to {filename}")
            
        elif command.lower() == 'backup_csv':
            filename = input("Enter filename for backup CSV: ")
            rent_service.save_to_backup_csv(filename)
            print(f"Backup saved to {filename}")



if __name__ == "__main__":
    main()