# doanAI_canhan

# Nhóm Thuật toán không có thông tin 
Thuật toán tìm kiếm không có thông tin (uninformed search) là nhóm thuật toán không sử dụng thông tin tiên đoán nào về vị trí đích ngoài việc biết trạng thái ban đầu và điều kiện dừng. 
1. Breadth-First Search (BFS)
BFS duyệt đồ thị theo chiều rộng, nghĩa là mở rộng tất cả các node ở độ sâu hiện tại trước khi đi sâu hơn. Thuật toán này sử dụng hàng đợi (queue) để quản lý các node cần duyệt. BFS đảm bảo tìm được đường đi ngắn nhất nếu chi phí các bước bằng nhau. Tuy nhiên, nó tiêu tốn nhiều bộ nhớ do phải lưu trữ toàn bộ các node ở mỗi mức.

3. Depth-First Search (DFS)
DFS duyệt theo chiều sâu, đi sâu vào một nhánh cho đến khi không thể đi tiếp rồi mới quay lại. Thuật toán có thể được triển khai bằng ngăn xếp hoặc đệ quy. DFS sử dụng ít bộ nhớ hơn BFS, nhưng không đảm bảo tìm được đường đi ngắn nhất và dễ bị rơi vào vòng lặp nếu không kiểm tra trạng thái đã duyệt.

4. Uniform Cost Search (UCS)
UCS là phiên bản tổng quát hơn của BFS, sử dụng hàng đợi ưu tiên để luôn mở rộng node có chi phí tích lũy thấp nhất. UCS đảm bảo tìm được đường đi có chi phí tối ưu, bất kể chi phí mỗi bước là bao nhiêu. Nhược điểm là tiêu tốn nhiều tài nguyên khi không gian trạng thái lớn.

5. Iterative Deepening DFS (IDDFS)
IDDFS kết hợp giữa DFS và BFS: nó thực hiện DFS nhiều lần với độ sâu giới hạn tăng dần. Mỗi vòng lặp là một DFS có giới hạn độ sâu cụ thể. IDDFS sử dụng bộ nhớ ít như DFS và vẫn đảm bảo tìm được lời giải tối ưu như BFS nếu chi phí mỗi bước là như nhau. Tuy nhiên, nó lặp lại việc duyệt nên sẽ tốn thời gian hơn.


# Nhóm Thuật Toán tìm kiếm có thông tin (Informed Search)
Nhóm thuật toán này sử dụng hàm đánh giá chi phí giúp giảm số node cần tìm và giúp cho việc giải bài toán nhanh hơn.

1. Greedy
Thuật toán này đánh giá chi phí từ điểm hiện tại đến đích không quan tâm đến chi phí đã đi.
  Ưu điểm: tốc độ nhanh, trực quan.
  Nhược điểm: không tối ưu, không đầy đủ nếu có chu trình.

2. A*
Thuật toán này kết hợp giữa việc tính chi phí từ khi bắt đầu đến điểm hiện tại và chi phí từ điểm hiện tại đến đích
  Ưu điểm: tối ưu, đầy đủ nếu chọn h(n) đúng.
  Nhược điểm: tốn RAM, đặc biệt với không gian lớn

3. IDA*
Thuật toán này là việc kết hợp giữa thuật toán IDDFS và thuật toán A*. Thay vì dùng hàng đợi ưu tiên như A* thì IDA* dùng giới hạn f(n).Giới hạn f(n) sẽ tăng dần theo từng vòng lặp
  Ưu điểm: tiết kiệm bộ nhớ hơn A*.
  Nhược điểm: thời gian chạy có thể cao nếu không gian phức tạp. 

# Nhóm Thuật toán leo đồi 
Nhóm thuật toán này tập trung vào việc tìm nghiệm tốt nhất bằng cách cải thiện nghiệm hiện tại. Tuy nhiên các thuật toán trong đây thường bị một vấn đề là local.

1. Simple Hill Climbing
Thuật toán bắt đầu từ trạng thái ban đầu và liên tục chuyển sang trạng thái láng giềng có giá trị đánh giá cao hơn, cho đến khi không thể cải thiện nữa.
  Ưu điểm: đơn giản, nhanh.
  Nhược điểm: dễ mắc kẹt, không quay lại trạng thái cũ.

2. Steepest Hill Climbing
Thuật Toán này là biến thể cải tiến của Simple Hill Climbing. Thay vì chọn láng giềng đầu tiên tốt hơn, thuật toán duyệt tất cả các láng giềng và chọn cái tốt nhất (có giá trị đánh giá cao nhất).
  Ưu điểm: lựa chọn tối ưu tại mỗi bước, tiến xa hơn Simple HC.
  Nhược điểm: vẫn không tránh được bẫy local.

3. Stochastic Hill Climbing
Là biến thể của Hill Climbing, thay vì chọn tốt nhất trong các láng giềng, thuật toán chọn ngẫu nhiên một láng giềng tốt hơn hiện tại.
  Giúp tránh bẫy cục bộ so với Hill Climbing thường.
  Có tính ngẫu nhiên nên kết quả có thể khác nhau mỗi lần chạy.

4. Simulated Annealing
Là thuật toán mô phỏng quá trình luyện kim, cho phép chấp nhận nghiệm kém hơn một cách xác suất để thoát khỏi cực trị cục bộ.
  Ưu điểm: thoát được cạm bẫy local.
  Nhược điểm: cần điều chỉnh tham số (nhiệt độ ban đầu, tốc độ làm nguội).

5. Beam Search
Beam Search mở rộng từ BFS, nhưng chỉ giữ lại k node tốt nhất ở mỗi bước (beam width). Giảm chi phí bộ nhớ và thời gian, nhưng có thể bỏ lỡ lời giải tốt nếu k quá nhỏ.
  Là tìm kiếm theo chiều rộng có chọn lọc.
  Không đảm bảo tối ưu hoặc đầy đủ.

6. Genetic Algorithm (chưa làm)
Là thuật toán dựa trên di truyền học: mỗi nghiệm là một “cá thể”, qua các vòng chọn lọc, lai ghép (crossover) và đột biến (mutation) để tiến hóa nghiệm tốt hơn.
  Tốt cho các bài toán không gian lớn, rời rạc.
  Kết quả phụ thuộc vào cách mã hóa cá thể và hàm đánh giá.
