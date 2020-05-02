#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int num;//��ǥ���� ����, dp�迭 ���鶧 ī���� ����
int answer;//���� ��
vector<pair<int, int>> coordinate; //��ǥ�� ���� ����
int dp[10001];
int main()
{	
	for (int i = 1; i <= 10000; i++)
		dp[i] = 987654321;

	cin >> num; 
	for (int i = 0; i < num; i++)
	{
		int element1, element2;
		cin >> element1 >> element2;
		coordinate.push_back(pair<int, int>(element1, element2));
	}
	sort(coordinate.begin(), coordinate.end()); //x��ǥ �������� ����
	
	for (int j=1;j<=num;j++) //dp 1~num���� ����
	{
		int up = 0;
		for (int i = j-1; i >=0; i--) //���� �ݴ���ϸ� dp[0]=0�̾ 30line�� �׻� ó���ϴ°� �̴ϸ��� �ȴ�
		{
			up = max(up, 2*abs(coordinate[i].second)); //x��ǥ���� �Ÿ��� ��ŭ �Ƶ� �׻��̿� y��ǥ�� ��û ū�� ������ ������ �� ũ�Ƿ�
			int square = max(up,coordinate[j-1].first-coordinate[i].first);//y��ǥ�� ���� ū�Ŷ� i,j x��ǥ �Ÿ��� �� ū�� square
			dp[j] = min(dp[i] + square, dp[j]);//dp
		}
	}
	cout << dp[num] << endl;
	return 0;
}