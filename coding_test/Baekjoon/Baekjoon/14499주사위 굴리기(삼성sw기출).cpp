#include <iostream>
using namespace std;
int dice[7], temp[7], map[20][20]; //�ֻ����� �������� ����,�ֻ��� ���� ���纻 ,������ �������� ����
int N, M, x, y, order_num;// ����/ ���� / ���� ���� ��ǥ ���� ���� ��ǥ / ��� ���� 
int forward_direction;// �̵� ���� 
int main()
{
	cin >> N >> M >> x >> y >> order_num;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			cin >> map[i][j];

	for (int i = 0; i < order_num; i++)
	{
		for (int j = 1; j <= 6; j++)
			temp[j] = dice[j];

		bool valid_flag = 0; // ���� üũ �÷���
		cin >> forward_direction;//�̵����� �Է¹ޱ�
		switch (forward_direction)//�̵����⿡ ���� �ֻ��� ������ ���� �ٲ��ֱ�
		{
		case 1://����
			if (y + 1 <= M - 1)
			{
				y = y + 1;
				valid_flag = 1;
				dice[1] = temp[3];
				dice[4] = temp[1];
				dice[6] = temp[4];
				dice[3] = temp[6];

				break;
			}
			else
				break;
		case 2://����
			if (y - 1 >= 0)
			{
				y = y - 1;
				valid_flag = 1;
				dice[3] = temp[1];
				dice[1] = temp[4];
				dice[4] = temp[6];
				dice[6] = temp[3];
				break;
			}
			else
				break;
		case 3://����
			if (x - 1 >= 0)
			{
				x = x - 1;
				valid_flag = 1;
				dice[2] = temp[1];
				dice[6] = temp[2];
				dice[5] = temp[6];
				dice[1] = temp[5];
				break;
			}
			else
				break;


		case 4://����
			if (x + 1 <= N - 1)
			{
				x = x + 1;
				valid_flag = 1;
				dice[1] = temp[2];
				dice[2] = temp[6];
				dice[6] = temp[5];
				dice[5] = temp[1];
				break;
			}
			else
				break;
		}
		if (valid_flag)
		{
			if (map[x][y] == 0)
				map[x][y] = dice[6];
			else
			{
				dice[6] = map[x][y];
				map[x][y] = 0;
			}
			if (valid_flag) //���������� �� ���� ������ ���� ���
				cout << dice[1] << endl;
		}

	}
	return 0;
}