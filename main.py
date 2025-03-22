import streamlit as st

st.set_page_config(
    page_title="Scrum Framework",
    page_icon="assets/icons/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar - Mục lục
with st.sidebar:
    st.header("Mục lục")
    st.markdown("""
    <div class="toc">
        <p>I. Lý do chọn đề tài</p>
        <p>II. Scrum là gì?</p>
        <p>III. Scrum Team</p>
        <p>IV. Các sự kiện Scrum</p>
        <p>V. Scrum Artifacts</p>
        <p>VI. Lợi ích của Scrum Framework</p>
        <p>VII. Hạn chế và cách khắc phục</p>
        <p>VIII. Video mô tả</p>
        <p>IX. Kết luận</p>
        <p>X. Trích nguồn</p>
    </div>
    """, unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["Bài viết", "Video"])

# Tab 1 - Nội dung bài viết
with tab1:
    st.markdown("<h2 style='color: #FFC81B;'>SCRUM FRAMEWORK – PHƯƠNG PHÁP GIÚP QUẢN LÝ DỰ ÁN TỐI ƯU</h2>", unsafe_allow_html=True)
    st.markdown("#### **Thành viên thực hiện:**")
    st.markdown("""
    - *Hoàng Thị Khánh Linh – SE190721*  
    - *Đào Thị Út Trinh – SE196429*
    """)

    # TOÀN BỘ NỘI DUNG SCRUM FRAMEWORK

    st.markdown("---")
    st.markdown("""<h3>I. Lý do chọn đề tài</h3>""", unsafe_allow_html=True)
    st.markdown("""
Trong bối cảnh phát triển nhanh chóng  của ngành công nghệ thông tin hiện nay, các phương pháp quản lý dự án truyền 
thống đang dần bộc lộ nhiều hạn chế, đặc biệt là trong một môi trường đòi hỏi sự linh hoạt và tốc độ cao. 
Scrum Framework, một trong những phương pháp Agile phổ biến, đã và đang được áp dụng rộng rãi trong ngành công nghệ 
thông tin.

Theo báo cáo của State of Agile Report 2023, hơn 58% doanh nghiệp trên toàn cầu đã áp dụng Scrum như một phương pháp 
chính để quản lý dự án phần mềm, tuy nhiên, 35% trong số đó gặp khó khăn trong việc duy trì và phát huy tối đa hiệu quả 
của Scrum (Digital.ai, 2023). Tại Việt Nam, mặc dù có hơn 60% doanh nghiệp công nghệ đã thử nghiệm Scrum (TopDev, 2024), 
nhưng tỷ lệ thành công vẫn chưa đạt mức kỳ vọng do sự thiếu hụt nhân sự có chuyên môn Agile, văn hóa tổ chức chưa phù 
hợp và quy trình triển khai chưa đồng bộ.

Thực tế này đặt ra một vấn đề quan trọng: _Làm thế nào để triển khai Scrum hiệu quả trong doanh nghiệp Việt Nam nhằm tối 
ưu hóa quy trình làm việc và nâng cao chất lượng sản phẩm?_ Xuất phát từ nhu cầu thực tiễn đó, nghiên cứu này tập trung 
vào việc đánh giá tổng quan về Scrum Framework, phân tích các yếu tố ảnh hưởng đến việc triển khai mô hình này trong các 
doanh nghiệp, đồng thời đề xuất các giải pháp giúp tối ưu hóa hiệu quả áp dụng Scrum tại Việt Nam.

Việc nghiên cứu Scrum không chỉ giúp các doanh nghiệp công nghệ tối ưu hóa quy trình phát triển phần mềm mà còn có thể 
mở rộng ứng dụng sang các lĩnh vực khác như tài chính, giáo dục, sản xuất, nơi yêu cầu cao về sự linh hoạt và hiệu suất 
làm việc. Với tiềm năng và tầm quan trọng của Scrum, bài viết này sẽ mang lại những giá trị thiết thực trong việc nâng 
cao hiệu quả quản lý dự án và phát triển nguồn nhân lực Agile tại Việt Nam.
""")

    st.markdown("""<h3>II. Scrum là gì?</h3>""", unsafe_allow_html=True)
    st.markdown("""
**1. Khái niệm Scrum**

Scrum là một cách làm việc nhóm hiệu quả, giúp chia nhỏ công việc thành từng phần nhỏ để dễ dàng quản lý và cải tiến 
liên tục thông qua phản hồi. 

Đây là một khung làm việc thuộc Agile, mang lại đủ cấu trúc để các nhóm có thể áp dụng linh hoạt và tối ưu hóa theo nhu 
cầu riêng.

Agile là một tư duy làm việc, còn Scrum là một framework dựa trên nguyên tắc của Agile. Ngoài Scrum, còn nhiều phương 
pháp Agile khác như Kanban, Extreme Programming (XP), SAFe…

**2. Scrum Framework**

Scrum được giới thiệu lần đầu vào năm 1995 và được định nghĩa rõ ràng trong The Scrum Guide – tài liệu do hai nhà sáng 
lập Ken Schwaber và Jeff Sutherland biên soạn. Scrum xoay quanh một đội nhóm gồm Product Owner, Scrum Master và các 
Developer, mỗi người có vai trò cụ thể. Nhóm này tham gia vào năm sự kiện chính và tạo ra ba sản phẩm đầu ra.

Scrum không phải một từ viết tắt, mà lấy cảm hứng từ một chiến thuật trong môn bóng bầu dục, nơi cả đội cùng hợp sức để 
đưa bóng về phía trước. Tương tự, trong Scrum, cả nhóm làm việc cùng nhau để phát triển sản phẩm từng bước một.

Scrum là một quy trình dựa trên thực nghiệm, nơi các quyết định được đưa ra dựa trên quan sát, kinh nghiệm và thử 
nghiệm. Ba yếu tố quan trọng của Scrum là:

- Minh bạch 
- Kiểm tra 
- Thích nghi 

Việc làm theo chu kỳ nhỏ giúp nhóm có thể kiểm tra và điều chỉnh liên tục. Tuy nhiên, điều quan trọng nhất để Scrum hoạt 
động hiệu quả là niềm tin giữa các thành viên. Nếu thiếu niềm tin, nhóm dễ gặp căng thẳng và khó hoàn thành công việc 
suôn sẻ.

**3. Nguyên tắc và giá trị của Scrum**

Mô hình Scrum hoạt động dựa trên các nguyên tắc sau:

- Công việc được chia thành các Sprint (chu kỳ ngắn dưới một tháng), nơi nhóm tạo ra những phần giá trị cụ thể.
- Trong mỗi Sprint, nhóm nhận phản hồi và điều chỉnh sản phẩm cũng như quy trình làm việc.
- Nhóm Scrum bao gồm Scrum Master, Product Owner và Developer, chịu trách nhiệm chuyển đổi công việc thành kết quả cụ thể 
trong Sprint.
- Ngoài nhóm Scrum, còn có các bên liên quan như khách hàng, doanh nghiệp, người dùng... giúp kiểm tra kết quả và định 
hướng cho Sprint tiếp theo.

**4. Scrum chuyên nghiệp**

Không phải cứ làm theo các bước trong Scrum là đủ. Để thực sự hiệu quả, nhóm cần có tư duy đúng đắn, xây dựng môi trường 
làm việc dựa trên niềm tin và các giá trị của Scrum: Dũng cảm, Tập trung, Cam kết, Tôn trọng, Cởi mở 

Những giá trị này đặc biệt quan trọng khi nhóm thử nghiệm và điều chỉnh cách làm việc. Nếu chỉ thực hiện các bước một 
cách máy móc mà không thực sự hiểu tư duy Scrum, nhóm sẽ dễ rơi vào tình trạng “làm cho có” mà không đạt được hiệu quả 
cao nhất.
""")

    st.markdown("""<h3>III. Scrum Team</h3>""", unsafe_allow_html=True)
    st.markdown("""
1. Scrum Team là gì?	

Scrum Team là nhóm làm việc cốt lõi trong Scrum, bao gồm Scrum Master, Product Owner và Developers. Trong nhóm Scrum, 
không có cấp bậc hay nhóm nhỏ, mà tất cả cùng hướng đến một mục tiêu chung: Product Goal.

2. Đặc điểm của Scrum Team

**Tính đa chức năng:** Các thành viên có đầy đủ kỹ năng để hoàn thành công việc trong mỗi Sprint.

**Tự quản lý:** Nhóm tự quyết định ai làm gì, khi nào và như thế nào.

**Quy mô nhỏ nhưng hiệu quả:** Nhóm thường có dưới 10 người, đủ nhỏ để linh hoạt nhưng đủ lớn để hoàn thành khối lượng công 
việc quan trọng. Nếu nhóm quá lớn, có thể chia thành nhiều nhóm Scrum nhỏ nhưng vẫn hướng đến cùng một sản phẩm.

**Chịu trách nhiệm toàn diện:** Nhóm chịu trách nhiệm không chỉ về phát triển sản phẩm, mà còn về làm việc với các bên liên 
quan, kiểm thử, bảo trì, nghiên cứu, vận hành, thử nghiệm…

Mỗi Sprint, nhóm Scrum có trách nhiệm tạo ra một phần sản phẩm có giá trị và có thể sử dụng được.

**3. Các vai trò trong Scrum Team**

**3.1. Developers**

Đây là những người trực tiếp xây dựng sản phẩm trong mỗi Sprint. Công việc của họ có thể bao gồm lập trình, thiết kế, 
kiểm thử, viết tài liệu… Tùy theo dự án mà kỹ năng của Developers sẽ khác nhau.

Họ có trách nhiệm:

- Lập kế hoạch cho Sprint - Sprint Backlog.
- Đảm bảo chất lượng bằng cách tuân theo Definition of Done.
- Cập nhật kế hoạch hằng ngày để đạt Sprint Goal. 
- Hỗ trợ lẫn nhau và chịu trách nhiệm về công việc chung.

**3.2. Product Owner**

Product Owner chịu trách nhiệm tối đa hóa giá trị của sản phẩm bằng cách quản lý Product Backlog.

**Nhiệm vụ chính của Product Owner:**

- Xác định và truyền đạt Product Goal rõ ràng.
- Tạo, sắp xếp và mô tả các Product Backlog Items.
- Đảm bảo Product Backlog luôn minh bạch, rõ ràng và dễ hiểu.

Product Owner là người duy nhất có quyền thay đổi thứ tự ưu tiên trong Product Backlog. Dù có thể ủy quyền cho người 
khác thực hiện công việc, nhưng vẫn phải chịu trách nhiệm chính.

**Lưu ý:** Product Owner không phải là một nhóm hay hội đồng. Đây là một cá nhân duy nhất, đại diện cho nhu cầu của nhiều 
bên liên quan. Nếu ai đó muốn thay đổi Product Backlog, họ phải thuyết phục Product Owner.

**3.3. Scrum Master**

Scrum Master chịu trách nhiệm giúp nhóm hiểu và áp dụng Scrum đúng cách, đồng thời đảm bảo hiệu quả làm việc của nhóm.

**Scrum Master hỗ trợ Scrum Team bằng cách:**
- Huấn luyện nhóm về tự quản lý và làm việc đa chức năng.
- Giúp nhóm tập trung vào việc tạo ra những phần sản phẩm có giá trị cao.
- Loại bỏ trở ngại ảnh hưởng đến tiến độ công việc.
- Đảm bảo các sự kiện Scrum diễn ra đúng quy trình và hiệu quả.

**Scrum Master hỗ trợ Product Owner bằng cách:**
- Hướng dẫn cách xác định Product Goal và quản lý Product Backlog hiệu quả.
- Giúp nhóm hiểu rõ yêu cầu công việc để có Product Backlog chất lượng.
- Hỗ trợ lập kế hoạch sản phẩm trong môi trường phức tạp.
- Tạo điều kiện hợp tác giữa Product Owner và các bên liên quan. 
**Scrum Master hỗ trợ tổ chức bằng cách:**
- Hướng dẫn, đào tạo và hỗ trợ doanh nghiệp áp dụng Scrum.
- Lên kế hoạch và triển khai Scrum trong tổ chức.
- Giúp nhân viên và các bên liên quan hiểu cách làm việc theo mô hình Scrum.
- Gỡ bỏ rào cản giữa nhóm Scrum và các bên liên quan.

    """)

    st.markdown("""<h3>IV. Các sự kiện Scrum</h3>""", unsafe_allow_html=True)
    st.markdown("""

Trong Scrum, các sự kiện đóng vai trò quan trọng trong việc tạo ra tính nhất quán, giúp các nhóm làm việc hiệu quả hơn 
và giảm thiểu những cuộc họp không cần thiết. Các sự kiện này không chỉ giúp duy trì nhịp điệu làm việc, mà còn là những 
cơ hội quan trọng để kiểm tra và thích ứng với sản phẩm cũng như quy trình làm việc. 

Sprint là một khung chứa tất cả các sự kiện khác, đảm bảo rằng mọi hoạt động trong Scrum đều diễn ra một cách có hệ 
thống và minh bạch. Khi các sự kiện được thực hiện đúng cách, chúng không chỉ tối ưu hóa quy trình phát triển mà còn 
giúp nhóm tận dụng tối đa khả năng học hỏi và cải tiến liên tục.

**1. Sprint là gì?**

Sprint là nhịp đập của Scrum, nơi các ý tưởng được chuyển hóa thành giá trị thực tế. Đây là một chu kỳ làm việc có thời 
gian cố định, tối đa một tháng, giúp duy trì tính nhất quán, phản hồi liên tục và giảm thiểu rủi ro. Khi một Sprint kết 
thúc, Sprint mới bắt đầu ngay lập tức.
Trong Sprint, tất cả công việc cần thiết để đạt **Product Goal** đều diễn ra, bao gồm:
- Sprint Planning
- Daily Scrum
- Sprint Review
- Sprint Retrospective

**Quy tắc trong Sprint:**

- Không thay đổi ảnh hưởng đến Sprint Goal.
- Đảm bảo chất lượng sản phẩm.
- Tinh chỉnh Product Backlog khi cần.
- Có thể điều chỉnh phạm vi công việc với Product Owner

Sprint giúp Scrum Team kiểm tra và thích ứng liên tục để đạt được Product Goal và Mục tiêu Sprint. Nhóm có thể chọn độ 
dài Sprint phù hợp, miễn là không quá một tháng. Các Sprint ngắn giúp tăng chu kỳ học hỏi và giảm rủi ro.

![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/Sprint.png)

**2. Sprint Planning là gì?**

Sprint Planning là sự kiện mở đầu của Sprint, nơi toàn bộ nhóm cùng nhau lên kế hoạch cho công việc thực hiện trong Sprint.

Sprint Planning sẽ tập trung vào 3 câu hỏi chính:

**Sprint này mang lại giá trị gì?**
    
- Product Owner đề xuất cách cải thiện giá trị sản phẩm trong Sprint.
- Nhóm Scrum thảo luận và xác định Sprint Goal, giúp truyền đạt giá trị Sprint đến các bên liên quan.
    
**Có thể hoàn thành những gì trong Sprint?**
- Developers chọn các mục từ Product Backlog để đưa vào Sprint.
- Các mục này có thể được điều chỉnh để tăng mức độ hiểu biết và sự tự tin về khả năng hoàn thành.
**Làm thế nào để hoàn thành công việc đã chọn?**    
- Developers lên kế hoạch triển khai từng mục tiêu đã chọn, có thể chia nhỏ công việc thành các phần nhỏ hơn.
- Nhóm có quyền tự quyết định cách thực hiện, không ai ngoài họ có thể áp đặt phương pháp làm việc.

Sprint Backlog bao gồm Sprint Goal, các mục tiêu từ Product Backlog đã chọn, và kế hoạch thực hiện.

Sprint Planning **giới hạn thời gian tối đa là 8 giờ** cho **Sprint kéo dài một tháng.** Nếu Sprint ngắn hơn, thời gian lập kế 
hoạch cũng sẽ được rút ngắn tương ứng.

![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/SprintPlanning.png)

**3. Daily Scrum là gì?**

Daily Scrum là cuộc họp 15 phút diễn ra hằng ngày trong Sprint, nơi Developers kiểm tra tiến độ và điều chỉnh kế hoạch 
nếu cần. Cuộc họp giúp nhóm tập trung vào Sprint Goal và lập kế hoạch hành động cho ngày làm việc tiếp theo.

**Trong mỗi cuộc họp của Daily Scrum phải trả lời 3 câu hỏi:**

- Hôm qua tôi đã làm gì để giúp nhóm đạt được mục tiêu Sprint?
- Hôm nay tôi sẽ làm gì để giúp nhóm đạt được mục tiêu Sprint?
- Có vấn đề gì cản trở tôi hoặc nhóm trong việc hoàn thành công việc không?

**Vai trò của Scrum Master:**
- Đảm bảo cuộc họp diễn ra đúng kế hoạch.
- Hướng dẫn nhóm giữ thời gian họp **không quá 15 phút.**
- Đảm bảo không ai ngoài nhóm làm gián đoạn cuộc họp.

**4. Sprint Review là gì?**

Sprint Review là sự kiện đánh giá kết quả Sprint và xác định điều chỉnh cần thiết cho tương lai. Scrum Team trình bày 
kết quả làm việc cho các bên liên quan và thảo luận về tiến độ đạt được đối với Product Goal.

**Mục tiêu của Sprint Review:**

- Kiểm tra những gì đã hoàn thành và những gì chưa hoàn thành.
- Xác định các thay đổi cần thiết trong Product Backlog.
- Đánh giá tác động từ thị trường và người dùng.
- Cung cấp thông tin quan trọng cho Sprint Planning tiếp theo.

**Nội dung chính:**
- Người tham gia: Scrum Team và các bên liên quan do Product Owner mời.
- Developers trình bày những công việc đã hoàn thành và cách giải quyết các vấn đề.
- Product Owner cập nhật trạng thái Product Backlog và dự đoán tiến độ.
- Cả nhóm cùng thảo luận về hướng đi tiếp theo.

**Sprint Review** là sự kiện **áp chót** của Sprint, có **giới hạn thời gian tối đa 4 giờ** cho Sprint kéo dài một tháng (Sprint 
ngắn hơn sẽ có thời gian họp ngắn hơn).
**Kết quả:**
- Product Backlog được cập nhật với các ưu tiên mới.
- Điều chỉnh kế hoạch để tối ưu hóa giá trị sản phẩm.

**5. Sprint Retrospective là gì?**

Sprint Retrospective là sự kiện cuối cùng trong Sprint, giúp Scrum Team đánh giá cách làm việc của nhóm để cải thiện 
chất lượng và hiệu suất cho các Sprint tiếp theo.

**Mục tiêu của Sprint Retrospective:**
- Xem xét lại cách nhóm làm việc trong Sprint vừa qua.
- Xác định điểm mạnh và những vấn đề cần cải thiện.
- Đưa ra cam kết thay đổi để làm việc hiệu quả hơn.

**Nội dung chính:**
- Scrum Team phân tích những gì đã làm tốt, những khó khăn gặp phải và cách giải quyết chúng.
- Xác định các cải tiến quan trọng nhất và ưu tiên triển khai sớm.
- Có thể điều chỉnh Definition of Done để nâng cao chất lượng sản phẩm.

**Vai trò của Scrum Master:**
- Hướng dẫn nhóm tìm ra cách cải tiến quy trình làm việc.
- Đảm bảo Sprint Retrospective giúp nhóm thích ứng và phát triển.
 
Giới hạn thời gian: Tối đa 3 giờ cho Sprint kéo dài một tháng (Sprint ngắn hơn thì họp ngắn hơn).

**Kết quả:**
- Scrum Team xác định các cải tiến sẽ thực hiện trong Sprint tiếp theo.
- Đây là cơ hội chính thức để kiểm tra và điều chỉnh cách làm việc của nhóm.

    """)

    st.markdown("""<h3>V. Scrum Artifacts</h3>""", unsafe_allow_html=True)
    st.markdown("""
Scrum Artifact giúp minh bạch hóa công việc và đo lường tiến độ. Mỗi artifact có một Commitment để đảm bảo tính tập 
trung và rõ ràng:

- Product Backlog → Commitment: Product Goal
- Sprint Backlog → Commitment: Sprint Goal
- Increment → Commitment: Definition of Done

**1.Product Backlog là gì?**

![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/ProductBacklog.png)

Product Backlog là danh sách có thứ tự ưu tiên, chứa tất cả các công việc cần thiết để cải thiện sản phẩm. Đây là nguồn 
công việc duy nhất của Scrum Team.

**Quản lý Product Backlog:**
- Các mục có thể hoàn thành trong một Sprint sẽ được chọn trong Sprint Planning.
- Product Backlog Refinement giúp chia nhỏ và làm rõ công việc, diễn ra liên tục để tăng tính minh bạch.
- Developers chịu trách nhiệm đánh giá kích thước công việc, còn Product Owner hỗ trợ ưu tiên và định hướng.
- Nếu nhiều Scrum Team cùng làm việc, họ sử dụng một Product Backlog chung.

**Cam kết: Product Goal**
- Product Goal xác định trạng thái tương lai của sản phẩm và hướng dẫn Scrum Team lập kế hoạch.
- Product Backlog phản ánh những gì cần làm để đạt được Product Goal.
- Scrum Team phải hoàn thành hoặc từ bỏ một Product Goal trước khi bắt đầu mục tiêu mới.

**Tóm lại:** Product Backlog giúp quản lý công việc linh hoạt, đảm bảo Scrum Team tập trung vào các mục tiêu quan trọng nhất 
để tạo ra giá trị cho sản phẩm. 

![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/ProducBackLog1.png)

**2. Sprint Backlog là gì?**

![Sprint](https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/images/SprintBacklog.png)

**2.1. Sprint Backlog là gì?**

Theo Scrum Guide, Sprint Backlog bao gồm:
- _Sprint Goal - Tại sao?_
- _Các mục từ Product Backlog được chọn cho Sprint (Cái gì?)_
- _Kế hoạch hành động để hoàn thành Increment (Làm thế nào?)_

Sprint Backlog là một kế hoạch do các Developer tự quản lý. Đây là bức tranh thời gian thực về công việc họ sẽ thực hiện 
trong Sprint để đạt được Sprint Goal. Sprint Backlog liên tục được cập nhật trong suốt Sprint khi có thêm thông tin mới. Nó cần đủ chi tiết để giúp nhóm kiểm tra tiến độ trong Daily Scrum.

**2.2. Cam kết: Sprint Goal**
- Sprint Goal là mục tiêu chính của Sprint.
- Nó là một cam kết của Developer, nhưng vẫn có tính linh hoạt về công việc cụ thể để đạt được nó.
- Sprint Goal giúp đội Scrum làm việc có trọng tâm, tránh phân tán vào các nhiệm vụ riêng lẻ.
- Được thiết lập trong Sprint Planning và thêm vào Sprint Backlog.
- Nếu công việc thay đổi so với dự kiến, nhóm có thể thương lượng lại phạm vi Sprint Backlog và Product Owner mà không làm 
ảnh hưởng đến Sprint Goal.

**2.3. Increment**

- Increment là một bước tiến cụ thể hướng tới Product Goal.
- Mỗi Increment phải có thể sử dụng và được kiểm tra kỹ lưỡng để đảm bảo tích hợp với các Increment trước đó.
- Có thể có nhiều Increment trong một Sprint, và tổng hợp chúng lại để trình bày trong Sprint Review.
- Một Increment có thể được phát hành tới khách hàng trước khi Sprint kết thúc.
- Công việc chỉ được coi là một phần của Increment nếu nó đáp ứng Definition of Done.

**3. Product Goal là gì?**

**3.1. Product Goal là gì?**

- Product Goal định hướng cho Product Backlog, mô tả trạng thái tương lai của sản phẩm.
- Đây là mục tiêu dài hạn của Scrum Team.
- Các mục trong Product Backlog giúp hiện thực hóa Product Goal theo thời gian, dựa trên việc học hỏi qua từng Sprint.
- Nó là một tuyên bố ngắn gọn, định hướng và tạo mục đích làm việc cho Scrum Team và các bên liên quan.
- Product Owner chịu trách nhiệm tạo ra và truyền đạt Product Goal.

**3.2. Đặc điểm của Product Goal**

- Chỉ có một Product Goal tại một thời điểm trong Product Backlog.
- Product Backlog thay đổi theo thời gian, phản ánh quá trình học hỏi của Scrum Team về sản phẩm và cách phát triển sản phẩm.
- Mỗi Increment được tạo ra trong Sprint giúp sản phẩm tiến gần hơn đến Product Goal.
- Product Goal được thể hiện rõ ràng trong Product Backlog, tương tự như cách Sprint Goal được thể hiện trong Sprint Backlog.

**3.3. Product Goal và Sprint Review**

Trong Sprint Review, Scrum Team cùng các bên liên quan sẽ đánh giá Increment và tiến độ đạt được đối với Product Goal.

Sprint Review giúp đặt bối cảnh cho các thảo luận về tiến độ và đưa ra các câu hỏi quan trọng.

Những phát hiện từ Sprint Review sẽ ảnh hưởng đến Sprint Planning cho Sprint tiếp theo, giúp xác định trọng tâm công việc.

**4. Definition of Done?**

**4.1. Definition of Done  là gì?**

Nếu bạn mới bắt đầu sử dụng Scrum, bạn sẽ nghe rất nhiều về khái niệm "Done" và "Definition of Done". Hãy hình dung 
"Done" là tất cả những yếu tố cần có để một Increment được xem là hoàn chỉnh.

Definition of Done (DoD) là một cam kết của Developers đối với Increment, giống như Sprint Goal là cam kết đối với 
Sprint Backlog, và Product Goal là cam kết của Product Owner đối với Product Backlog.

Scrum Guide mô tả Definition of Done là một mô tả chính thức về trạng thái của Increment khi nó đáp ứng các tiêu chuẩn 
chất lượng cần thiết. Khi một Increment đạt đến trạng thái Done, nó có thể được bàn giao hoặc phát hành.

**4.2. Lợi ích của Definition of Done**

- **Tạo sự minh bạch:** Mọi người có cùng hiểu biết về công việc đã hoàn thành và các tiêu chuẩn cần đáp ứng.
- **Kiểm soát chất lượng:** Nếu một Product Backlog Item chưa đáp ứng Definition of Done, nó không thể được phát hành.
- **Đảm bảo tuân thủ tiêu chuẩn:** Nếu tổ chức có các tiêu chuẩn chất lượng riêng, tất cả các Scrum Teams phải tuân theo. 
Nếu không có, nhóm Scrum tự thiết lập tiêu chuẩn phù hợp với sản phẩm.

**4.3. Cách tạo Definition of Done**

Nhóm Scrum có thể làm việc cùng nhau để xác định các tiêu chí cần thiết. Một số nhóm có thể sử dụng các phương pháp tư 
duy sáng tạo như Liberating Structures để xác định Definition of Done.

Dưới đây là một số ví dụ về các tiêu chí có thể có trong Definition of Done:

**Ví dụ cho một ứng dụng phần mềm y tế**
- Hoàn thành tất cả các bài kiểm thử.
- Không có lỗi được biết đến.
- Đã hoàn thành và vượt qua quy trình kiểm tra mã nguồn (code review).
- Đáp ứng tiêu chuẩn bảo mật.
- Tuân thủ các yêu cầu bảo mật chung.

Khi tất cả tiêu chí trong _Definition of Done_ được đáp ứng, Increment được coi là _Done_. Trong các dự án phức tạp, 
Definition of Done có thể được mở rộng để đảm bảo các tiêu chuẩn chất lượng nghiêm ngặt hơn.

    """)

    st.markdown("""<h3>VI. Lợi ích của Scrum Framework</h3>""", unsafe_allow_html=True)
    st.markdown("""
    
**1. Tăng khả năng thích ứng và linh hoạt **

- Scrum giúp nhóm phản ứng nhanh với sự thay đổi yêu cầu từ khách hàng hoặc thị trường.
- Thay vì lên kế hoạch cố định dài hạn, nhóm làm việc theo từng Sprint ngắn (thường là 2-4 tuần), dễ dàng điều chỉnh hướng 
đi khi cần.

**2. Cải thiện hiệu suất và tốc độ phát triển** 

- Nhóm chỉ tập trung vào các công việc quan trọng trong Sprint hiện tại, tránh lãng phí thời gian vào những tính năng 
không cần thiết.
- Scrum khuyến khích các cuộc họp ngắn hằng ngày (Daily Scrum) giúp nhanh chóng phát hiện và giải quyết vấn đề.

**3. Tăng chất lượng sản phẩm **

- Mỗi Increment (phần sản phẩm hoàn thành) phải đáp ứng tiêu chuẩn Definition of Done, đảm bảo chất lượng trước khi phát 
hành.
- Scrum tạo điều kiện cho phản hồi sớm từ khách hàng hoặc người dùng, giúp cải thiện sản phẩm liên tục.

**4. Minh bạch và cải thiện sự phối hợp trong nhóm **

- Tất cả thành viên đều có chung hiểu biết về tiến độ công việc thông qua các Artifact như Product Backlog, Sprint 
Backlog, và Increment.
- Cuộc họp Sprint Review giúp nhóm đánh giá kết quả, còn Sprint Retrospective giúp nhóm cải thiện cách làm việc.

**5. Giảm rủi ro **

- Scrum giúp phát hiện và xử lý rủi ro sớm nhờ cách làm việc theo chu kỳ ngắn.
- Thay vì đợi đến cuối dự án để kiểm tra, Scrum liên tục cung cấp các phiên bản sản phẩm nhỏ nhưng có thể sử dụng được.

**6. Tăng sự hài lòng của khách hàng**

- Scrum đảm bảo rằng sản phẩm phát triển theo đúng nhu cầu khách hàng thông qua phản hồi liên tục.
- Scrum không chỉ tập trung vào việc hoàn thành công việc mà còn đặt giá trị sản phẩm và trải nghiệm người dùng lên hàng 
đầu.

**7. Cải thiện động lực và trách nhiệm của nhóm**

- Scrum tạo ra môi trường tự quản lý, nơi nhóm quyết định cách thực hiện công việc thay vì bị áp đặt từ trên xuống.
- Sự tham gia chủ động của nhóm giúp họ có trách nhiệm hơn với công việc.

    """)

    st.markdown("""<h3>VII. Hạn chế và cách khắc phục</h3>""", unsafe_allow_html=True)
    st.markdown("""
Scrum là một khung làm việc mạnh mẽ giúp các nhóm phát triển phần mềm trở nên linh hoạt, phản ứng nhanh với thay đổi và 
tối ưu hóa quy trình làm việc. Tuy nhiên, nó cũng có một số giới hạn và hạn chế nhất định, đặc biệt đối với các nhóm mới 
hoặc trong môi trường không lý tưởng. Dưới đây là các hạn chế chính của Scrum và phân tích lý do vì sao chúng có thể gây 
ra thách thức.

**1. Thiếu hướng dẫn về cách trưởng thành của đội ngũ từ khởi đầu đến khi hoàn thiện.**


**1.1. Hạn chế**

Scrum tập trung vào các nguyên tắc cốt lõi như tự tổ chức, tính minh bạch và cải tiến liên tục, nhưng nó không cung cấp 
một lộ trình rõ ràng để giúp một nhóm non trẻ phát triển từ một nhóm mới hình thành đến một nhóm Scrum thực sự hiệu quả.

**1.2. Tại sao đây là vấn đề?**

- Các nhóm mới vào có thể gặp khó khăn khi tự tổ chức do thiếu kinh nghiệm làm việc theo mô hình Agile.
- Scrum không có hướng dẫn cụ thể về cách xây dựng năng lực nhóm theo thời gian.
- Nếu không có một Scrum Master hoặc người hướng dẫn có kinh nghiệm, nhóm có thể gặp khó khăn trong việc định hướng, dẫn 
đến việc áp dụng Scrum không hiệu quả.

**1.3. Giải pháp khắc phục**

- Áp dụng mô hình Tuckman Model: Giúp đội ngũ hiểu các giai đoạn phát triển từ Forming → Storming→ Norming → Performing.
- Huấn luyện và đào tạo Scrum Master để hướng dẫn nhóm vượt qua các rào cản ban đầu.

**2. Thiếu tự chủ và kinh nghiệm trong đội ngũ phát triển**

**2.1. Hạn chế**

Scrum đòi hỏi các nhóm phải tự tổ chức và có trách nhiệm cao, nhưng không phải đội nào cũng có sẵn tư duy này. Những 
nhóm mới hoặc những người quen làm việc theo cách truyền thống (Waterfall) có thể gặp khó khăn khi chuyển sang cách làm 
việc tự chủ.

**2.2. Tại sao đây là vấn đề?**

- Một nhóm chưa có kinh nghiệm Scrum có thể không biết cách tự phân công công việc hoặc không rõ ai chịu trách nhiệm 
chính.
- Nếu không có sự hướng dẫn từ Scrum Master, nhóm có thể rơi vào tình trạng hỗn loạn, dẫn đến chậm tiến độ hoặc làm việc 
kém hiệu quả.
- Các thành viên có thể thiếu kỹ năng giao tiếp và ra quyết định nhanh trong nhóm tự tổ chức.

**2.3. Giải pháp khắc phục**

- Huấn luyện về Agile mindset cho đội ngũ để nâng cao khả năng tự tổ chức.
- Scrum Master nên đóng vai trò người hướng dẫn thay vì chỉ là người điều phối – giúp nhóm phát triển tư duy tự chủ.
- Tổ chức các buổi workshop về giao tiếp nhóm và ra quyết định nhanh trong Scrum để cải thiện kỹ năng làm việc nhóm.

**3. Scrum chỉ là khung làm việc, không cung cấp đầy đủ công cụ và quy trình chi tiết**

**3.1. Hạn chế**

Scrum chỉ đưa ra các nguyên tắc và khung làm việc, không cung cấp một hướng dẫn đầy đủ về cách thực hiện từng bước trong 
quy trình phát triển phần mềm.

**3.2. Tại sao đây là vấn đề?**

- Scrum không quy định công cụ nào nên dùng, cách quản lý tài nguyên, hay cách đo lường hiệu suất nhóm.
- Các nhóm có thể cảm thấy lạc lõng nếu không có sự chuẩn bị trước về công cụ và quy trình bổ sung.
- Scrum không có hướng dẫn cụ thể về quản lý ngân sách, quản lý rủi ro, hay kế hoạch dự phòng – điều này có thể gây khó 
khăn cho các tổ chức lớn hoặc các dự án phức tạp.

**3.3. Giải pháp khắc phục**

- Sử dụng các công cụ quản lý dự án như Jira, Trello hoặc Azure DevOps để theo dõi tiến độ công việc.
- Tích hợp mô hình DevOps để hỗ trợ triển khai và duy trì sản phẩm hiệu quả hơn.

**4. Tự quản lý là yếu tố quan trọng nhưng không phải nhóm nào cũng có thể áp dụng dễ dàng**

**4.1. Hạn chế**

Scrum yêu cầu nhóm phát triển phải tự quản lý công việc của mình mà không có sự giám sát chặt chẽ từ bên ngoài. Tuy 
nhiên, trong thực tế, không phải nhóm nào cũng có thể áp dụng mô hình này một cách trơn tru.

**4.2. Tại sao đây là vấn đề?**

- Nếu các thành viên trong nhóm không quen với việc đưa ra quyết định độc lập, tiến độ công việc có thể bị đình trệ.
- Một số nhóm vẫn quen với cách làm việc chỉ huy – phản hồi, nên khó thích nghi với Scrum.
- Nếu không có Scrum Master đủ kinh nghiệm, nhóm có thể mất phương hướng hoặc đi lệch khỏi mục tiêu ban đầu.

**4.3. Giải pháp khắc phục**

- Tổ chức các buổi huấn luyện về kỹ năng tự quản lý và ra quyết định nhóm.
- Áp dụng kỹ thuật Lean Agile Leadership, nơi quản lý đóng vai trò hỗ trợ thay vì kiểm soát.
- Sử dụng các OKRs (Objectives and Key Results) để giúp nhóm có định hướng rõ ràng mà vẫn giữ được sự tự chủ.

    """)

    st.markdown("""<h3>VIII. Video mô tả quy trình làm việc Scrum trong Jira</h3>""", unsafe_allow_html=True)
    st.markdown("""Jira là một công cụ phổ biến được Atlassian phát triển để hỗ trợ quản lý dự án theo Scrum, giúp lập 
    kế hoạch, theo dõi và quản lý các nhiệm vụ trong nhóm.
    
    [Scrum Framework trong Jira.mp4](https://drive.google.com/file/d/1egH6nyQmaXCtzAuqVhKfGydTZzpF8bOy/view)
    """)

    st.markdown("""<h3>IX. Kết luận</h3>""", unsafe_allow_html=True)
    st.markdown("""
Scrum là một trong những khung làm việc Agile phổ biến và hiệu quả nhất trong phát triển phần mềm cũng như các lĩnh vực 
khác đòi hỏi sự linh hoạt và khả năng thích nghi cao. Với các nguyên tắc cốt lõi như tính minh bạch, thanh tra và thích 
ứng, Scrum giúp nhóm làm việc một cách linh hoạt, tối ưu hóa quy trình phát triển và phản hồi nhanh chóng với các thay 
đổi của thị trường.

Tuy nhiên, Scrum không phải là một giải pháp toàn diện cho mọi vấn đề. Nó đặt ra những thách thức nhất định như yêu cầu 
cao về tự tổ chức, thiếu hướng dẫn chi tiết cho nhóm mới, và sự phụ thuộc vào cam kết của các bên liên quan. Để triển 
khai Scrum thành công, tổ chức cần hiểu rõ các hạn chế của nó và có các biện pháp khắc phục phù hợp, như đào tạo đội 
ngũ, kết hợp Scrum với các mô hình bổ trợ (XP, Kanban), và sử dụng các công cụ quản lý Agile.

Mặc dù có những hạn chế, nhưng nếu được áp dụng đúng cách, Scrum có thể giúp các nhóm nâng cao năng suất, cải thiện chất 
lượng sản phẩm và tối đa hóa giá trị mang lại cho khách hàng. Đây không chỉ là một phương pháp làm việc mà còn là một 
triết lý giúp doanh nghiệp xây dựng văn hóa đổi mới, linh hoạt và hiệu suất cao trong môi trường hiện đại.

    """)

    st.markdown("""<h3>X. Trích nguồn</h3>""", unsafe_allow_html=True)
    st.markdown("""
**Scrum.org. (n.d.).** _What is Scrum?_ Scrum.org. Retrieved March 6, 2025, from [https://www.scrum.org/learning-series/what-is-scrum/](https://www.scrum.org/learning-series/what-is-scrum/)

**GeeksforGeeks. (n.d.).** _What is Scrum?_ GeeksforGeeks. Retrieved March 6, 2025, from [https://www.geeksforgeeks.org/what-is-scrum/](https://www.geeksforgeeks.org/what-is-scrum/)

**Atlassian. (n.d.).** _What is Scrum?_ Atlassian. Retrieved March 6, 2025, from [https://www.atlassian.com/agile/scrum](https://www.atlassian.com/agile/scrum)

**ScrumLife.** (2023, October 10). _Scrum in 20 mins… (with examples)_ [Video]. YouTube. Retrieved March 6, 2025, from [https://www.youtube.com/watch?v=SWDhGSZNF9M](https://www.youtube.com/watch?v=SWDhGSZNF9M)

**Tony Teaches Tech.** (2023, August 15). _HOW TO USE JIRA | Free Agile Project Management Software (Jira tutorial for Beginners)_** [Video]. YouTube. Retrieved March 6, 2025, from [https://www.youtube.com/watch?v=GWxMTvRGlpc](https://www.youtube.com/watch?v=GWxMTvRGlpc)

_MUST-KNOW Jira features for Scrum Masters_ [Video]. YouTube. Retrieved March 6, 2025, from [https://www.youtube.com/watch?v=issdcnErAU8](https://www.youtube.com/watch?v=issdcnErAU8)

**Figma. (n.d.).** _SCRUM Pricing Calculator._ Figma. Retrieved March 6, 2025, from [https://www.figma.com/file/I79KrKItmi3lrzfTIMlyto/SCRUM-Pricing-Calculator?node-id=0%3A1](https://www.figma.com/file/I79KrKItmi3lrzfTIMlyto/SCRUM-Pricing-Calculator?node-id=0%3A1)

**Figma. (n.d.).** _Pricing Calculator SCRUM._ Figma. Retrieved March 6, 2025, from [https://www.figma.com/board/U1U3Rsksylm7znnS6O8Oi0/Pricing-Calculator-SCRUM?node-id=0-1&p=f&t=yNehZlNUtz4eamA0-0](https://www.figma.com/board/U1U3Rsksylm7znnS6O8Oi0/Pricing-Calculator-SCRUM?node-id=0-1&p=f&t=yNehZlNUtz4eamA0-0)

**Ong Dev. (n.d.).** _Scrum cơ bản | Quy trình phát triển phần mềm_ [Video]. YouTube. Retrieved March 6, 2025, from [https://www.youtube.com/watch?v=KmOKQS9u-90](https://www.youtube.com/watch?v=KmOKQS9u-90)

**Malmstadt, J. (2023, December 15).** _Does Scrum have limitations or gaps it can't solve?_ Scrum.org. Retrieved March 6, 2025, from [https://www.scrum.org/resources/blog/does-scrum-have-limitations-or-gaps-it-cant-solve](https://www.scrum.org/resources/blog/does-scrum-have-limitations-or-gaps-it-cant-solve)

    """)

# Tab 2 - Video
with tab2:
    st.subheader("Video mô tả quy trình làm việc Scrum trong Jira")
    st.video("https://raw.githubusercontent.com/KietPham-VN/TechAwayScrum/main/assets/")

