

# Trình Văn Lưu MSSV: 23110260
# 1. Mục Tiêu
1. Mục tiêu tổng quát:
    Đồ án nhằm nghiên cứu, phân tích và ứng dụng các thuật toán trí tuệ nhân tạo (AI) vào các bài toán thực tế, từ đó nâng cao hiểu biết về cách thức hoạt động, ưu – nhược điểm và phạm vi áp dụng của từng nhóm thuật toán. Mỗi nhóm sinh viên sẽ phụ trách nghiên cứu và trình bày một lớp thuật toán khác nhau trong lĩnh vực AI.

2. Mục tiêu cụ thể :
    1. Phân chia 6 nhóm thuật toán chính trong AI, mỗi nhóm đảm nhận một hướng nghiên cứu riêng biệt:
        + Thuật toán tìm kiếm không thông tin
        + Thuật toán tìm kiếm có thông tin 
        + Thuật toán leo đồi
        + Thuật toán học củng cố 
        + Thuật toán trong môi trường có ràng buộc 
        + Thuật toán trong môi trường không xác định

    2. Áp dụng từng thuật toán vào game 8 puzzle
    3. So sánh

# 2. Nội dung 
# 2.1. Nhóm Thuật toán không có thông tin 
Thuật toán tìm kiếm không có thông tin (uninformed search) là nhóm thuật toán không sử dụng thông tin tiên đoán nào về vị trí đích ngoài việc biết trạng thái ban đầu và điều kiện dừng. 
1. Breadth-First Search (BFS)
BFS duyệt đồ thị theo chiều rộng, nghĩa là mở rộng tất cả các node ở độ sâu hiện tại trước khi đi sâu hơn. Thuật toán này sử dụng hàng đợi (queue) để quản lý các node cần duyệt. BFS đảm bảo tìm được đường đi ngắn nhất nếu chi phí các bước bằng nhau. Tuy nhiên, nó tiêu tốn nhiều bộ nhớ do phải lưu trữ toàn bộ các node ở mỗi mức.

![BFS](https://github.com/user-attachments/assets/638f7d33-a19e-467b-84e8-99c55604f42d)

2. Depth-First Search (DFS)
DFS duyệt theo chiều sâu, đi sâu vào một nhánh cho đến khi không thể đi tiếp rồi mới quay lại. Thuật toán có thể được triển khai bằng ngăn xếp hoặc đệ quy. DFS sử dụng ít bộ nhớ hơn BFS, nhưng không đảm bảo tìm được đường đi ngắn nhất và dễ bị rơi vào vòng lặp nếu không kiểm tra trạng thái đã duyệt.

![DFS-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/96c3628b-d19c-49a9-842b-6c2fb67ffe3b)

3. Uniform Cost Search (UCS)
UCS là phiên bản tổng quát hơn của BFS, sử dụng hàng đợi ưu tiên để luôn mở rộng node có chi phí tích lũy thấp nhất. UCS đảm bảo tìm được đường đi có chi phí tối ưu, bất kể chi phí mỗi bước là bao nhiêu. Nhược điểm là tiêu tốn nhiều tài nguyên khi không gian trạng thái lớn.

![UCS-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/cc9a1d57-e3d8-4eff-8152-f2b2d3036ba3)

4. Iterative Deepening DFS (IDDFS)
IDDFS kết hợp giữa DFS và BFS: nó thực hiện DFS nhiều lần với độ sâu giới hạn tăng dần. Mỗi vòng lặp là một DFS có giới hạn độ sâu cụ thể. IDDFS sử dụng bộ nhớ ít như DFS và vẫn đảm bảo tìm được lời giải tối ưu như BFS nếu chi phí mỗi bước là như nhau. Tuy nhiên, nó lặp lại việc duyệt nên sẽ tốn thời gian hơn.

![IDDFS](https://github.com/user-attachments/assets/4d817569-77e2-44d2-92c6-0259a65fdb5e)

- So sánh Chung:

  +  BFS (Breadth-First Search):
    Tìm kiếm theo chiều rộng, đảm bảo tìm được lời giải tối ưu nếu chi phí các bước bằng nhau. Tuy nhiên, tiêu tốn nhiều bộ nhớ vì phải lưu toàn bộ các node theo từng mức.
    
    +  DFS (Depth-First Search):
    Tìm kiếm theo chiều sâu, tiết kiệm bộ nhớ, dễ cài đặt. Nhưng không đảm bảo tìm đường đi ngắn nhất và dễ rơi vào vòng lặp nếu không kiểm tra trạng thái đã duyệt.
    
    + UCS (Uniform Cost Search):
    Mở rộng node có chi phí tích lũy thấp nhất, luôn tìm được đường đi tối ưu. Tuy nhiên, tốn tài nguyên và thời gian nếu không gian trạng thái quá lớn.
    
  + IDDFS (Iterative Deepening DFS):
    Kết hợp ưu điểm của DFS và BFS: tiết kiệm bộ nhớ và vẫn đảm bảo tìm lời giải tối ưu nếu chi phí đều. Nhược điểm là phải duyệt lại nhiều lần nên chậm hơn.

# 2.2. Nhóm Thuật Toán tìm kiếm có thông tin (Informed Search)
Nhóm thuật toán này sử dụng hàm đánh giá chi phí giúp giảm số node cần tìm và giúp cho việc giải bài toán nhanh hơn.

1. Greedy
Thuật toán này đánh giá chi phí từ điểm hiện tại đến đích không quan tâm đến chi phí đã đi.
    + Ưu điểm: tốc độ nhanh, trực quan.
    + Nhược điểm: không tối ưu, không đầy đủ nếu có chu trình.

![Greedy](https://github.com/user-attachments/assets/c8895463-eb3b-4376-8606-98b2751ad1e8)

2. A*
Thuật toán này kết hợp giữa việc tính chi phí từ khi bắt đầu đến điểm hiện tại và chi phí từ điểm hiện tại đến đích
    + Ưu điểm: tối ưu, đầy đủ nếu chọn h(n) đúng.
    + Nhược điểm: tốn RAM, đặc biệt với không gian lớn

![A_star-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/d3abb93c-0287-445a-a318-83acd6330acf)

3. IDA*
Thuật toán này là việc kết hợp giữa thuật toán IDDFS và thuật toán A*. Thay vì dùng hàng đợi ưu tiên như A* thì IDA* dùng giới hạn f(n).Giới hạn f(n) sẽ tăng dần theo từng vòng lặp
    + Ưu điểm: tiết kiệm bộ nhớ hơn A*.
    + Nhược điểm: thời gian chạy có thể cao nếu không gian phức tạp. 

![IDA_star](https://github.com/user-attachments/assets/11f54a08-13ee-4a42-9480-39319ea2b92b)

# 2.3. Nhóm Thuật toán leo đồi 
Nhóm thuật toán này tập trung vào việc tìm nghiệm tốt nhất bằng cách cải thiện nghiệm hiện tại. Tuy nhiên các thuật toán trong đây thường bị một vấn đề là local.

1. Simple Hill Climbing
Thuật toán bắt đầu từ trạng thái ban đầu và liên tục chuyển sang trạng thái láng giềng có giá trị đánh giá cao hơn, cho đến khi không thể cải thiện nữa.
    + Ưu điểm: đơn giản, nhanh.
    + Nhược điểm: dễ mắc kẹt, không quay lại trạng thái cũ.

![SimpleHC-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/fbd84ce6-2f5c-4d8a-9a1b-126585b66afe)

2. Steepest Hill Climbing
Thuật Toán này là biến thể cải tiến của Simple Hill Climbing. Thay vì chọn láng giềng đầu tiên tốt hơn, thuật toán duyệt tất cả các láng giềng và chọn cái tốt nhất (có giá trị đánh giá cao nhất).
    + Ưu điểm: lựa chọn tối ưu tại mỗi bước, tiến xa hơn Simple HC.
    + Nhược điểm: vẫn không tránh được bẫy local.

![HC](https://github.com/user-attachments/assets/a84b3d4d-3517-4631-a8cd-684e0c42666e)

3. Stochastic Hill Climbing
Là biến thể của Hill Climbing, thay vì chọn tốt nhất trong các láng giềng, thuật toán chọn ngẫu nhiên một láng giềng tốt hơn hiện tại.
    + Giúp tránh bẫy cục bộ so với Hill Climbing thường.
    + Có tính ngẫu nhiên nên kết quả có thể khác nhau mỗi lần chạy.

![SHC](https://github.com/user-attachments/assets/65736b18-1327-4a0d-946b-a29c92c9445a)

4. Simulated Annealing
Là thuật toán mô phỏng quá trình luyện kim, cho phép chấp nhận nghiệm kém hơn một cách xác suất để thoát khỏi cực trị cục bộ.
    + Ưu điểm: thoát được cạm bẫy local.
    + Nhược điểm: cần điều chỉnh tham số (nhiệt độ ban đầu, tốc độ làm nguội).

![SA](https://github.com/user-attachments/assets/0288dd71-eb45-4ea6-a6db-0416f7ec0aee)

5. Beam Search
Beam Search mở rộng từ BFS, nhưng chỉ giữ lại k node tốt nhất ở mỗi bước (beam width). Giảm chi phí bộ nhớ và thời gian, nhưng có thể bỏ lỡ lời giải tốt nếu k quá nhỏ.
    + Là tìm kiếm theo chiều rộng có chọn lọc.
    + Không đảm bảo tối ưu hoặc đầy đủ.

![Beam-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/df66048b-80e7-4cb5-a7af-58e8b2c2a086)

6. Genetic Algorithm (chưa làm)
Là thuật toán dựa trên di truyền học: mỗi nghiệm là một “cá thể”, qua các vòng chọn lọc, lai ghép (crossover) và đột biến (mutation) để tiến hóa nghiệm tốt hơn.
    + Tốt cho các bài toán không gian lớn, rời rạc.
    + Kết quả phụ thuộc vào cách mã hóa cá thể và hàm đánh giá.

![GA](https://github.com/user-attachments/assets/0b7cd804-5b5e-4d86-8a55-05cbef6eb351)

# 2.4. Nhóm Thuật toán trong môi trường không xác định 
1. AND OR SEARCH
    + OR-node: Đại diện cho lựa chọn giữa các hành động khác nhau.
    + AND-node: Đại diện cho các điều kiện con đều phải được thỏa mãn để giải quyết bài toán
    + Ưu điểm: Mô hình hóa được cả lựa chọn (OR) và ràng buộc (AND), giúp xử lý các vấn đề phức tạp.
    + Nhược điểm: Cây tìm kiếm có thể rất lớn, khó triển khai và hình dung.

![AndOr](https://github.com/user-attachments/assets/a54f9332-8c77-4a6e-99cd-10702d596f25)

2. Belief State 
    Thuật toán này là thuật toán dùng để giải khi không biết bất cứ thông tin gì về môi trường. Giả định mình trong một môi trường và tìm ra lời giải
    + Ưu điểm: Giải được bài toán trong môi trường hoàn toàn không rõ ràng.
    + Nhược điểm: Không gian trạng thái cực kỳ lớn, dễ nổ bộ nhớ.

![NiemTin](https://github.com/user-attachments/assets/d2b93550-ee99-4968-bafa-dc4aee2ee5b9)

3. Niềm tin một phần
    Thuật toán này cũng như thuật toán của môi trường niềm tin, nhưng điểm khác biệt là sẽ có một số thông tin được thấy rõ. Việc còn lại là giả định các thông tin khác tạo nên môi trường và giải.
    + Ưu điểm: Thực tế hơn khi có cảm biến, giảm số lượng trạng thái cần xét so với belief state hoàn toàn.
    + Nhược điểm: Vẫn phức tạp, đòi hỏi phải tính toán trên không gian giả định.

![NiemTinMotPhan](https://github.com/user-attachments/assets/cc71eaa1-b65e-4c65-a279-1999ea4b7578)

# 2.5. Nhóm thuật toán ràng buộc 
Trong đồ án này thì nhóm thuật toán ràng buộc bao gồm có kiểm thử, backtracking và AC3
1. Kiểm thử
Thuật toán sẽ thử tất cả các giá trị rồi kiểm tra điều kiện, nếu không thoả điều kiện thì sẽ bỏ trường hợp đó. Kết quả là một tập các ma trận thoả điều kiện của thuật toán

![KiemThu](https://github.com/user-attachments/assets/87d781a5-8763-4d09-856d-f71a4e027874)

2. Backtracking
Thuật toán cũng như kiểm thử nhưng khác ở chỗ kiểm thử sẽ đặt hết giá trị rồi mới xét ràng buộc trong khi đó Backtracking dùng đệ quy để quay lui lại. trong quá trình quay lui nếu thầy ma trận hiện tại có một tiêu chí không thoả điều kiện thì sẽ break nhánh đó và nhảy sang nhánh khác để xét tiếp

![BackTracking-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/3d102abd-139d-4791-b26c-ae9486a6dbad)

3. AC3
Thuật toán này cũng như hai cái trên. Mà AC3 dựa vào điều kiện hạn chế các giá trị có thể xuất hiện của mỗi biến trước rồi dựa vào đó mà tìm mà trận thoả yêu cầu

+ So sánh nhanh:
    + Kiểm thử: Tiền đề, nhưng thiếu hiệu quả trong quy mô lớn.

    + Backtracking: Tối ưu không gian tìm kiếm bằng cách “cắt nhánh sớm”, ứng dụng rộng rãi trong AI, game, giải bài toán tổ hợp.
    
    + AC3: Thuật toán thông minh lọc miền giá trị, kết hợp với backtracking giúp tạo ra bộ công cụ cực kỳ mạnh trong Constraint Satisfaction Problems (CSP).



![AC3](https://github.com/user-attachments/assets/51a223d6-be7d-407b-a294-bef1c31a43b0)

# 2.6. Nhóm Thuật toán củng cố 
Thuật toán học củng cố (Reinforcement Learning – RL) thuộc nhóm học có mục tiêu (goal-directed learning) trong Machine Learning, nơi mà tác nhân (agent) học cách hành động tối ưu trong một môi trường thông qua phần thưởng (reward) nhận được sau mỗi hành động.
1. Q learning
Q-Learning là một thuật toán Model-Free Reinforcement Learning, giúp agent học cách tối ưu hành động trong môi trường bằng cách cập nhật bảng giá trị (Q-table), mà không cần biết trước mô hình môi trường.Mục tiêu: Học ra hàm Q(s, a) = giá trị kỳ vọng của việc thực hiện hành động a tại trạng thái s, rồi từ đó chọn hành động tối ưu.
Công thức cập nhật Q:
    + Q(s,a) = Q(s,a) + alpha*(reward + gamma* max(Q(s',a')) - Q(s,a))
Với:
        + alpha là learning rate
        + reward là phần thưởng
        + gamma là khoảng cách
        + s' là trạng thái mới
- Ưu Điểm:
        + Dễ hiểu – dễ cài	
        + Không cần mô hình môi trường	
        + Học được chính sách tối ưu	
        + Tốt cho không gian trạng thái nhỏ	
- Nhược điểm:
        + Học chậm trong môi trường phức tạp
        + Không mở rộng tốt cho bài toán

![QLearning1](https://github.com/user-attachments/assets/9fcffb77-2e8e-4569-a672-dfad757592fe)

![Qlearning2](https://github.com/user-attachments/assets/418c7a7d-4b53-4662-86fd-c0e9877c981d)

# 3. Kết Luận 
Trong quá trình làm project em đã hiểu thêm về các thuật toán trong môn trí tuệ nhân tạo. Em đã áp dụng được các thuật toán vào game 8 puzzles. Qua đó có thể thấy được thuật toán nào tối ưu có thể được áp dụng vào game. Bên cạnh đó em cũng đã phải chăm chút từng lỗi trong quá trình code. Nhờ đó mà cải thiện tư duy cũng như kĩ năng lập trình.
