#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100 // Tamanho máximo para cada entrada

// Funções
void add_password();
void view_passwords();
void delete_password();
void delete_individual_password();

int main(void)
{
    int choice;

    do {
        printf("\n*** Gerenciador de Senhas ***\n");
        printf("1. Adicionar senha\n");
        printf("2. Ver senhas\n");
        printf("3. Excluir senha individual\n");
        printf("0. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &choice);
        getchar();  // Para capturar o \n deixado no buffer pelo scanf

        switch (choice)
        {
            case 1:
                add_password();
                break;
            case 2:
                view_passwords();
                break;
            case 3:
                delete_individual_password();
                break;
            case 0:
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida!\n");
        }
    } while (choice != 0);

    return 0;
}

// Função para adicionar uma senha
void add_password()
{
    char service[MAX];
    char username[MAX];
    char password[MAX];

    printf("Nome do serviço: ");
    fgets(service, MAX, stdin);
    service[strcspn(service, "\n")] = 0;  // Remove o newline do fgets

    printf("Nome de usuário: ");
    fgets(username, MAX, stdin);
    username[strcspn(username, "\n")] = 0;  // Remove o newline do fgets

    printf("Senha: ");
    fgets(password, MAX, stdin);
    password[strcspn(password, "\n")] = 0;  // Remove o newline do fgets

    // Abre o arquivo em modo de adição
    FILE *file = fopen("passwords.txt", "a");
    if (file == NULL)
    {
        printf("Erro ao abrir o arquivo!\n");
        return;
    }

    // Escreve as informações no arquivo de forma padronizada
    fprintf(file, "Usuário: %s\nServiço: %s\nSenha: %s\n---\n", username, service, password);
    fclose(file);

    printf("Senha adicionada com sucesso!\n");
}

// Função para visualizar todas as senhas agrupadas por usuário
void view_passwords()
{
    char line[MAX];
    char current_user[MAX] = "";
    FILE *file = fopen("passwords.txt", "r");

    if (file == NULL)
    {
        printf("Nenhuma senha armazenada ou erro ao abrir o arquivo.\n");
        return;
    }

    printf("\n*** Senhas Armazenadas ***\n");

    while (fgets(line, sizeof(line), file))
    {
        if (strncmp(line, "Usuário:", 8) == 0)
        {
            // Detecta um novo usuário e imprime o nome
            strcpy(current_user, line);
            printf("\n%s", current_user);  // Exibe o nome do usuário
        }
        else if (strncmp(line, "---", 3) != 0)
        {
            // Exibe as informações de serviços e senhas, omitindo linhas de separação
            printf("%s", line);
        }
    }

    fclose(file);
}

// Função para excluir uma senha individualmente por serviço
void delete_individual_password()
{
    char service[MAX], username[MAX];
    char line[MAX];
    int found = 0;

    printf("Nome do serviço que deseja excluir: ");
    fgets(service, MAX, stdin);
    service[strcspn(service, "\n")] = 0;

    printf("Nome do usuário: ");
    fgets(username, MAX, stdin);
    username[strcspn(username, "\n")] = 0;

    FILE *file = fopen("passwords.txt", "r");
    FILE *temp = fopen("temp.txt", "w");

    if (file == NULL || temp == NULL)
    {
        printf("Erro ao abrir o arquivo.\n");
        return;
    }

    while (fgets(line, sizeof(line), file))
    {
        // Se encontramos o serviço e o usuário, pulamos as linhas associadas a eles
        if (strstr(line, username) && found == 0)
        {
            found = 1;
        }

        if (found && strstr(line, service))
        {
            // Encontrou o serviço a ser excluído, pula 2 linhas (senha e separador)
            fgets(line, sizeof(line), file);  // Senha
            fgets(line, sizeof(line), file);  // Separador
            found = 0;
        }
        else
        {
            // Copia todas as outras linhas para o arquivo temporário
            fputs(line, temp);
        }
    }

    fclose(file);
    fclose(temp);

    // Remove o arquivo original e renomeia o temporário para substituir o original
    remove("passwords.txt");
    rename("temp.txt", "passwords.txt");

    printf("Senha excluída com sucesso!\n");
}
