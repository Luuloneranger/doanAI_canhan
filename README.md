# doanAI_canhan

#Nhóm Thuật toán không có thông tin 
Thuật toán tìm kiếm không có thông tin (uninformed search) là nhóm thuật toán không sử dụng thông tin tiên đoán nào về vị trí đích ngoài việc biết trạng thái ban đầu và điều kiện dừng. 
1. Breadth-First Search (BFS)
BFS duyệt đồ thị theo chiều rộng, nghĩa là mở rộng tất cả các node ở độ sâu hiện tại trước khi đi sâu hơn. Thuật toán này sử dụng hàng đợi (queue) để quản lý các node cần duyệt. BFS đảm bảo tìm được đường đi ngắn nhất nếu chi phí các bước bằng nhau. Tuy nhiên, nó tiêu tốn nhiều bộ nhớ do phải lưu trữ toàn bộ các node ở mỗi mức.



3. Depth-First Search (DFS)
DFS duyệt theo chiều sâu, đi sâu vào một nhánh cho đến khi không thể đi tiếp rồi mới quay lại. Thuật toán có thể được triển khai bằng ngăn xếp hoặc đệ quy. DFS sử dụng ít bộ nhớ hơn BFS, nhưng không đảm bảo tìm được đường đi ngắn nhất và dễ bị rơi vào vòng lặp nếu không kiểm tra trạng thái đã duyệt.

4. Uniform Cost Search (UCS)
UCS là phiên bản tổng quát hơn của BFS, sử dụng hàng đợi ưu tiên để luôn mở rộng node có chi phí tích lũy thấp nhất. UCS đảm bảo tìm được đường đi có chi phí tối ưu, bất kể chi phí mỗi bước là bao nhiêu. Nhược điểm là tiêu tốn nhiều tài nguyên khi không gian trạng thái lớn.

5. Iterative Deepening DFS (IDDFS)
IDDFS kết hợp giữa DFS và BFS: nó thực hiện DFS nhiều lần với độ sâu giới hạn tăng dần. Mỗi vòng lặp là một DFS có giới hạn độ sâu cụ thể. IDDFS sử dụng bộ nhớ ít như DFS và vẫn đảm bảo tìm được lời giải tối ưu như BFS nếu chi phí mỗi bước là như nhau. Tuy nhiên, nó lặp lại việc duyệt nên sẽ tốn thời gian hơn.

So sánh nhanh:
BFS: tìm đường đi ngắn nhất (khi chi phí bằng nhau), tốn nhiều bộ nhớ.
DFS: nhanh và tiết kiệm bộ nhớ, nhưng không đảm bảo tối ưu.
UCS: tìm đường đi có chi phí thấp nhất, dùng được với trọng số khác nhau.
IDDFS: tối ưu và tiết kiệm bộ nhớ, phù hợp với không gian tìm kiếm rộng và sâu.
