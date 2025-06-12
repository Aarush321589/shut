def shutdown(reason, delay, confirm_shutdown):
    """
    Simulates a computer shutdown using only function arguments.

    Arguments:
    - reason: Explanation for shutdown.
    - delay: Seconds to wait before 'shutdown'.
    - confirm_shutdown: True to proceed with 'shutdown', False to cancel.
    """
    print("========================================")
    print("⚠️  SYSTEM SHUTDOWN INITIATED ⚠️")
    print("========================================")
    print("Reason:", reason)
    print("Shutdown will occur in", delay, "seconds.")
    print("----------------------------------------")

    if not confirm_shutdown:
        print("Shutdown aborted. System will continue to run.")
        return

    # Simulate the delay countdown (no real delay without time.sleep)
    for i in range(delay, 0, -1):
        print("Shutting down in", i, "seconds...")

    print("🔴 Executing simulated system shutdown now... Goodbye!")
    print("========================================")

# Example usage
def main():
    shutdown("Routine maintenance", 5, True)

if __name__ == "__main__":
    main()
