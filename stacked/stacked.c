#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// definitions
#define MAX_STRING 256

#define ANSI_COLOR_RED          "\x1b[31m"
#define ANSI_COLOR_GREEN        "\x1b[32m"
#define ANSI_COLOR_YELLOW       "\x1b[33m"
#define ANSI_COLOR_BLUE         "\x1b[34m"
#define ANSI_COLOR_MAGENTA      "\x1b[35m"
#define ANSI_COLOR_CYAN         "\x1b[36m"
#define ANSI_COLOR_RESET        "\x1b[0m"
#define ANSI_UNDERLINE          "\x1b[4m"
#define ANSI_UNDERLINE_RESET    "\x1b[24m"
#define ANSI_CURSOR_HOME        "\x1b[H"
#define ANSI_CLEAR              "\x1b[J"
#define PRESS_ENTER             "\n\nPress ENTER to continue..."

// function prototypes
void feedback(void);
void clearBuffer(void);
void clearScreen(void);
void menu(void);
void pressEnter(void);

// code
int main()
{
    setbuf(stdout, 0);
    clearScreen();
    printf(ANSI_COLOR_CYAN
           ANSI_UNDERLINE
           "Hello and welcome to the DiceSect notes app!\n\n"
           ANSI_COLOR_YELLOW
           ANSI_UNDERLINE_RESET
           "This application is still in alpha, and may contain some bugs.\n"
           ANSI_COLOR_RESET
           );
    pressEnter();
    menu();
    return 0;
}

void feedback(void)
{
    // char flag[] = "vuctf{flag_sanitised_for_your_protection!!}";
    char flag[] = "vuctf{the_odds_were_stacked_in_your_favour}";
    char more_filler[] = "almost there";
    char filler[] = "getting closer";
    char *name = malloc(MAX_STRING);
    if (name == NULL)
    {
        printf("Not allocated\n");
        exit(1);
    }

    printf(ANSI_COLOR_YELLOW "Please leave feedback for the creator of this app" ANSI_COLOR_RESET "\n> ");
    fgets(name, MAX_STRING, stdin);
    
    if ((strlen(name) > 0) && (name[strlen(name) - 1] == '\n'))
    {
        name[strlen(name) - 1] = '\0';
    }
    printf("\nThankyou, the following comment will be passed onto the creator of this application.\n\n");
    printf(name, name);

    free(name);
}

void menu(void)
{
    char choice;
    clearScreen();
    printf("What would you like to do?\n\n\t"
            ANSI_COLOR_YELLOW "[1]" ANSI_COLOR_RESET " View notes.\n\t"
            ANSI_COLOR_YELLOW "[2]" ANSI_COLOR_RESET " Add a note.\n\t"
            ANSI_COLOR_YELLOW "[3]" ANSI_COLOR_RESET " Quit the program\n\n"
            "Make a choice: ");
    choice = getchar();
    clearBuffer();
    switch (choice)
    {
        case '1':
            clearScreen();
            printf(
                ANSI_COLOR_RED
                "Currently there are 1 note\\s.\n\n"
                ANSI_COLOR_YELLOW
                "\tI seem to be having some issues with the feedback function when exiting,\n"
                "\tthere seems to be some strange output when certain characters are entered,\n"
                "\tit might be something to do with the printf statement."
                ANSI_COLOR_RESET
                );
            pressEnter();
            menu();
            break;
        case '2':
            clearScreen();
            printf(ANSI_COLOR_RED "ERROR" ANSI_COLOR_CYAN " - " ANSI_COLOR_YELLOW "Feature not implemented.\n" ANSI_COLOR_RESET);
            pressEnter();
            menu();
            break;
        default:
            printf("\nExiting application...\n\n");
            feedback();
            break;
    }
}

void pressEnter(void) 
{
    printf(ANSI_COLOR_GREEN PRESS_ENTER ANSI_COLOR_RESET);
    clearBuffer();
}
void clearBuffer(void) { while (getchar() != '\n'); }
void clearScreen(void) { printf(ANSI_CURSOR_HOME ANSI_CLEAR);}