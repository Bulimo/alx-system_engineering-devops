#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - infinite while loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - starting point of the program
 *
 * Return: always 0
 */
int main(void)
{
	pid_t pid = 0;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();

	return (0);
}
