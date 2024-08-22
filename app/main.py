import argparse, dao

def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    parser.add_argument('action', help='Action to perform (e.g., add, list, etc.)')
    parser.add_argument('params', nargs='*', help='Parameters for the action')

    if len(parser.parse_args().params) == 0 and parser.parse_args().action != 'list':
        parser.error("You must provide appropriate parameters for this action.")
    
    args = parser.parse_args()

    if args.action == 'add':
        if not args.params:
            parser.error("You must provide a task description to add.")
        dao.add_task(args.params[0])
    elif args.action == 'list':
        dao.list_tasks(*args.params)
    elif args.action == 'update':
        if len(args.params) < 2:
            parser.error("You need to provide an ID and a new description to update.")
        dao.update_task(int(args.params[0]), args.params[1])
    elif args.action == 'delete':
        if not args.params:
            parser.error("You need to provide the task ID to delete.")
        dao.delete_task(int(args.params[0]))
    elif args.action == 'mark-in-progress':
        if not args.params:
            parser.error("You need to provide the task ID to mark as in-progress.")
        dao.mark_task(int(args.params[0]), 'in-progress')
    elif args.action == 'mark-done':
        if not args.params:
            parser.error("You need to provide the task ID to mark as done.")
        dao.mark_task(int(args.params[0]), 'done')
    else:
        print("Invalid action.")


if __name__ == '__main__':
    main()
