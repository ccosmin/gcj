#include <iostream>
#include <string>
#include <set>

int InsertPaths(const std::string& path, std::set<std::string>& fs)
{
  int result = 0;
  std::size_t pos = 0;
  fs.insert("/");
  do
  {
    pos = path.find("/", pos + 1);
    std::string pathfragment = path.substr(0, pos != std::string::npos ? pos : path.size());
    if ( fs.insert(pathfragment).second )
      ++result;
  } while ( pos != std::string::npos );
  return result;
}

int main()
{
  int testcases;
  std::cin >> testcases;
  for ( int tc = 0; tc < testcases; ++tc )
  {
    int n;
    int m;
    std::cin >> n >> m;
    std::cin.ignore();
    std::set<std::string> s;
    for ( int k = 0; k < n; ++k )
    {
      std::string path;
      std::getline(std::cin, path);
      InsertPaths(path, s);
    }
    int sum = 0;
    for ( int k = 0; k < m; ++k )
    {
      std::string path;
      std::getline(std::cin, path);
      sum += InsertPaths(path, s);
    }
    std::cout << "Case #" << (tc + 1) << ": " << sum << std::endl;
  }
}

