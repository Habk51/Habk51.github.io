---
title: "Cách thêm nhanh bộ câu hỏi vào Anki | VANDUCWEB"
source: "https://55tm-github-io.pages.dev/docs/H%E1%BB%8CC/ANKI/them-cau-hoi"
author:
published:
created: 2025-05-19
description: "Tưởng tượng bạn đang ở trong một tình huống như sau: Bạn đã có sẵn một file đề cương dạng câu hỏi trắc nghiệm (như hình bên dưới), và bạn muốn đưa tất cả những câu hỏi này thành flashcard trong Anki nhưng lại không biết làm thế nào cho nhanh."
tags:
  - "clippings"
---
Tưởng tượng bạn đang ở trong một tình huống như sau: Bạn đã có sẵn một file đề cương dạng câu hỏi trắc nghiệm (như hình bên dưới), và bạn muốn đưa tất cả những câu hỏi này thành flashcard trong Anki nhưng lại không biết làm thế nào cho nhanh.

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhaLjJKUj2xA87EXMcOOEW2H2M1Dfbq-GL6pJhSv4Sp4A5ekwKyBOpUnC1DGd5wcO4n0ZgF9GGn7P\_ei3Ch86uSfeQ0Es5v1ELQZQ14l0gIiNxKJQfQzMLFQtRWy8dY8hzYaPbExEliXlqcglYsnacykcUwMri38wFvWsPcDI7w6CFMAltaR-F7HIIjS2e/s1391/Screenshot%202024-10-04%20145735.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhaLjJKUj2xA87EXMcOOEW2H2M1Dfbq-GL6pJhSv4Sp4A5ekwKyBOpUnC1DGd5wcO4n0ZgF9GGn7P_ei3Ch86uSfeQ0Es5v1ELQZQ14l0gIiNxKJQfQzMLFQtRWy8dY8hzYaPbExEliXlqcglYsnacykcUwMri38wFvWsPcDI7w6CFMAltaR-F7HIIjS2e/s1391/Screenshot%202024-10-04%20145735.png))

nguồn: yhoctructuyen.net

Copy-paste từng câu một thì quá lâu, chuyển thành dạng bảng spreadsheet (.csv) thì cũng... lâu không kém. Vậy phải làm như thế nào? Trong bài viết này, mình sẽ giới thiệu cho các bạn một cách mà mình hay sử dụng, mình thấy nó rất hiệu quả và mong rằng bạn cũng sẽ thấy vậy. Cùng bắt đầu nhé!

Bước 1: Chuẩn bị file bộ câu hỏi a. Xác định file mục tiêu Để import một bộ thẻ (deck) vào Anki, ngoài định dạng anki deck (.apkg) của Anki bạn có thể dùng các định dạng tệp khác, phổ biến nhất là dạng bảng (.csv) và dạng text (.txt). Cá nhân mình chủ yếu sử dụng dạng text bởi tính tiện lợi và gần gũi với các file bộ câu hỏi chúng ta thường dùng.

Có 2 điều bạn cần lưu ý khi import một file.txt vào anki:

- Một, Anki nhận biết thẻ trong file.txt bằng ký hiệu xuống dòng, tức mỗi dòng là một thẻ
- Hai, chúng ta cần phải xác định dấu phân tách câu hỏi và đáp án (field separator), tức là dấu hiệu để anki biết rằng đâu là mặt trước (câu hỏi) và đâu là mặt sau (đáp án) của thẻ. Hiện tại anki chấp nhận một số dấu phân cách gồm: tab, pipe (|), semicolon (;), colon (.), comma (,), và space (dấu cách)

Theo kinh nghiệm của mình, chúng ta nên dùng tab hoặc pipe bởi 2 dấu này rất ít sử dụng trong văn bản thông thường, do vậy anki sẽ không bị tách nhầm khi gặp phải các dấu câu còn lại xuất hiện trong bộ câu hỏi. Trong bài viết này, mình sẽ sử dụng tab, đây cũng là cách mình hay sử dụng, và nó cũng tiện hơn pipe.

Bạn có thể xem hình dưới để hiểu hơn về những gì mình vừa mô tả.

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkrB-F4XaJrludvljdy9DKzDOFi0YUYJom-meJbwxDEBFb-ogoKh6YV35MAJrRw5ZgIGcJSx9E7PHTWFS\_sDNbPtCm8tdInSdKR980BzZJlxC6roqrZBSjmMra\_\_0t9M\_un8ZpDdwPRSpRkdm2odtQMHx8Uq67f1uul\_89Tdlyhbcrp8ZyMjIWFZ4TZzqq/s924/Screenshot%202024-10-05%20094517.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkrB-F4XaJrludvljdy9DKzDOFi0YUYJom-meJbwxDEBFb-ogoKh6YV35MAJrRw5ZgIGcJSx9E7PHTWFS_sDNbPtCm8tdInSdKR980BzZJlxC6roqrZBSjmMra__0t9M_un8ZpDdwPRSpRkdm2odtQMHx8Uq67f1uul_89Tdlyhbcrp8ZyMjIWFZ4TZzqq/s924/Screenshot%202024-10-05%20094517.png))

Như vậy, tóm lại mục tiêu của chúng ta là biến file docx phía trên thành một file.txt với mỗi câu hỏi là một dòng và đáp án được tách ra bởi dấu tab.

b. Bắt đầu tạo file Để đạt được mục tiêu trên, ta cần dùng đến một chức năng rất hữu ích của Word đó là Find & Replace (phím tắt Ctrl + H). Để sử dụng chức năng này một cách hiệu quả nhất thì các câu hỏi trong bộ câu hỏi phải được trình bày theo một định dạng nhất định. Mình sẽ sử dụng định dạng sau:

Câu hỏi `Các đáp án <đáp án đúng>` Đây là bộ câu hỏi trên sau khi đã thêm đáp án và trình bày dưới định dạng này

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEii1a0XcLjKa3wh-Ugxp49tquCAGbcBu0mhVhZLguaYZjWe5nOlDHVb\_Y0RQchSPxgJf-aEn-n7WHtwSiRkvskwEhN5CdXc75UVBxLrhJSLxi2c9PWgb8nhyphenhyphenETDRSQwlQ8s9HyBi0jdNAE62kQf42dv6xRmdqfqjfUeZdDMO9GIsdXE5nkeHk\_FU0Qh8NrW/s1360/Screenshot%202024-10-04%20153223.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEii1a0XcLjKa3wh-Ugxp49tquCAGbcBu0mhVhZLguaYZjWe5nOlDHVb_Y0RQchSPxgJf-aEn-n7WHtwSiRkvskwEhN5CdXc75UVBxLrhJSLxi2c9PWgb8nhyphenhyphenETDRSQwlQ8s9HyBi0jdNAE62kQf42dv6xRmdqfqjfUeZdDMO9GIsdXE5nkeHk_FU0Qh8NrW/s1360/Screenshot%202024-10-04%20153223.png))

Phần đáp án đúng mình đang để trong 2 dấu

```markdown
<>,
```

tuy nhiên bạn có thể sử dụng bất kỳ dấu nào mà bạn muốn, miễn là các câu hỏi phải thống nhất cùng một định dạng, và phải có bắt đầu cũng như kết thúc đáp án, ví dụ @A@, ''A'',;;A;;, v.v.

Đến đây thì bạn có thể thắc mắc rằng "Ui cái công đoạn nhập đáp án này cũng hết hơi, không nhanh tí nào". Đúng là vậy nhưng đây là cách duy nhất, và kinh nghiệm ôn thi của mình cũng cho thấy rằng chúng ta nên học file.docx hoặc.pdf trước khi học bằng Anki, để rà soát được một lượt xem bộ câu hỏi của ta có những gì, nó có vấn đề gì không để kịp thời sửa chữa luôn. Và trong quá trình học ấy ta có thể lồng ghép việc điền đáp án vào luôn, như vậy việc điền đáp án không còn gọi là "tốn công" nữa.

Tiếp đến bạn lần lượt sử dụng Find & Replace theo các 3 bước sau (bên trái là Find, bên phải là Replace with):

`1. ^p     -->   <br> 2. <br><  -->   ^t 3. ><br>  -->   ^p` Chú thích:

Trong Word, ^p sẽ được hiểu là xuống dòng, ^t sẽ được hiểu là tab Trong Anki, là dấu hiệu xuống dòng, khi import vào Anki sẽ tự động mất đi và thay bằng xuống dòng Tada~ và đây là thành quả của các bước vừa rồi:

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglyqNIRAGdyaAVN36EuKemq3\_z3FxXtdW8QS2Ynp46DGfTEJm8wRPn34OZfx\_ARt0zpCROHg3TwvWWKNoYPKk0I3q9v27Am6XOavAoPtfKrrjXWHD2aT\_-gHQrJDP7pWJiowM8bl4AeV1hg0RrHvW6iLb\_ShyphenhyphenaV76Vrsx0EzuXGNXmv29ohc00iVMT7bx5/s637/Screenshot%202024-10-04%20154555.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglyqNIRAGdyaAVN36EuKemq3_z3FxXtdW8QS2Ynp46DGfTEJm8wRPn34OZfx_ARt0zpCROHg3TwvWWKNoYPKk0I3q9v27Am6XOavAoPtfKrrjXWHD2aT_-gHQrJDP7pWJiowM8bl4AeV1hg0RrHvW6iLb_ShyphenhyphenaV76Vrsx0EzuXGNXmv29ohc00iVMT7bx5/s637/Screenshot%202024-10-04%20154555.png))

Tiếp theo, trong Word, bạn chọn File > Save As, điền tên file rồi chọn định dạng file là Plain Text (.txt).

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMcjimqiNWejuKmxQZnPBAaEfulAxoCUF0KiPpJX1wwaKvEC\_iJ64jR65U-hp\_J-gBUQyTl2VBv9c4b7lYq2d\_XRmGB0d-nfSAvduh0keav0kya\_KDlVHoIeQ24iCp477oms4qThif2GBEnHYfJrlz9rx32tVBXCj4Ex0VfNqs1nR4pN4drFuU4R84A-EY/s700/Screenshot%202024-10-05%20100155.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMcjimqiNWejuKmxQZnPBAaEfulAxoCUF0KiPpJX1wwaKvEC_iJ64jR65U-hp_J-gBUQyTl2VBv9c4b7lYq2d_XRmGB0d-nfSAvduh0keav0kya_KDlVHoIeQ24iCp477oms4qThif2GBEnHYfJrlz9rx32tVBXCj4Ex0VfNqs1nR4pN4drFuU4R84A-EY/s700/Screenshot%202024-10-05%20100155.png))

Sau khi ấn Save, một cửa sổ hiện ra như dưới đây, bạn chọn Other encoding rồi trong ô bên tay phải kéo lên chọn Unicode (UTF-8). Vậy là xong bước chuẩn bị rồi đó.

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhphJoNVMZ8fufMexKFlbnebOUoLZexCdt-9kJ0VrscBNUIR4Wh8jaZbSQZpvpkiEQUbJLUOU6OwAfb8UZeGnrQc43f36uMKdQc4fRZ77z6j34MoIbS8HlxUxLFLHRjhRk1\_d6HWvCUIyqejVhy2sqiFX\_s28u3QrTm-J6W0GnXJEY0\_kIT4yum7myRWv3E/s527/Pasted%20image%2020241005100059.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhphJoNVMZ8fufMexKFlbnebOUoLZexCdt-9kJ0VrscBNUIR4Wh8jaZbSQZpvpkiEQUbJLUOU6OwAfb8UZeGnrQc43f36uMKdQc4fRZ77z6j34MoIbS8HlxUxLFLHRjhRk1_d6HWvCUIyqejVhy2sqiFX_s28u3QrTm-J6W0GnXJEY0_kIT4yum7myRWv3E/s527/Pasted%20image%2020241005100059.png))

Bước 2: Import vào Anki Và giờ là import file vừa rồi vào Anki. Trong giao diện chính của Anki, bạn chọn Import File rồi chọn file.txt đã tạo vừa rồi.

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGZlYgY4G7001RZHBc90OBt-aWbJp-yRkYwjTczdSs586ODupIsFMLw8oSogkLcF-R1aShw\_dBwDLAb-VIQcm3uLiEvf51gjeJF7Pkr4a0VU0Atx9CGH5m85n780YVjrQHsVw\_zozi7Grp6XmRwBQ4jTUsAAHxtXFfloZXm0XnFV-4vuaJBfoajpvLVLPU/s947/Pasted%20image%2020241004155508.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGZlYgY4G7001RZHBc90OBt-aWbJp-yRkYwjTczdSs586ODupIsFMLw8oSogkLcF-R1aShw_dBwDLAb-VIQcm3uLiEvf51gjeJF7Pkr4a0VU0Atx9CGH5m85n780YVjrQHsVw_zozi7Grp6XmRwBQ4jTUsAAHxtXFfloZXm0XnFV-4vuaJBfoajpvLVLPU/s947/Pasted%20image%2020241004155508.png))

Giao diện Import File bật lên, bạn lưu ý (1) chọn Field separator là Tab (hoặc Pipe nếu bạn dùng Pipe), (2) Notetype để Basic, (3) Deck là deck bạn muốn dùng để chứa bộ câu hỏi. Cuối cùng (4) bấm nút Import màu xanh phía trên.

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3jB8CTbn4a4MOXJfo0JnkI2MI8VlP2jpoItLGhwINwBA8wVuMX6vPtrGWWe-vbDI5kw-QCnxkPleI1YZ1iUq4M2f0taycYmqWjJm4QV\_NnDdRzCvZ4pa6-WQ80CqNwdpNU8Zey8Aw71J6vrXX\_C2c1IL0SNnfEKP2hgp95Zx3\_OPE0tioDyYKQ-QGRKH1/s800/Pasted%20image%2020241004155820.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3jB8CTbn4a4MOXJfo0JnkI2MI8VlP2jpoItLGhwINwBA8wVuMX6vPtrGWWe-vbDI5kw-QCnxkPleI1YZ1iUq4M2f0taycYmqWjJm4QV_NnDdRzCvZ4pa6-WQ80CqNwdpNU8Zey8Aw71J6vrXX_C2c1IL0SNnfEKP2hgp95Zx3_OPE0tioDyYKQ-QGRKH1/s800/Pasted%20image%2020241004155820.png))

Cửa sổ Overview hiện lên cho biết bạn đã import bao nhiêu câu hỏi, hãy bấm Show để xem qua một lượt xem các câu hỏi có lỗi gì không

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigEheusIpKUCAQh4jRAuLUQ4l8h-JwyCjOiY5Jc7PYFwFYM1HokbeaeOB2h9FlrRo2cQ9-Ppu\_ALPVfX6xyuLMAsa4McUBbxZz4MJYyJjlbU4tfq\_EIhyphenhyphenyVbJHNz9XFOhjxDxKSnXnI0hf8406NJyyGDgIszUcx\_Z63J8QAi1af4gAXlDUv9a0BZO7wSNa/s792/Screenshot%202024-10-04%20155906.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigEheusIpKUCAQh4jRAuLUQ4l8h-JwyCjOiY5Jc7PYFwFYM1HokbeaeOB2h9FlrRo2cQ9-Ppu_ALPVfX6xyuLMAsa4McUBbxZz4MJYyJjlbU4tfq_EIhyphenhyphenyVbJHNz9XFOhjxDxKSnXnI0hf8406NJyyGDgIszUcx_Z63J8QAi1af4gAXlDUv9a0BZO7wSNa/s792/Screenshot%202024-10-04%20155906.png))

Thứ tự câu hỏi trong deck cũng tương ứng với thứ tự câu hỏi trong file docx/pdf của bạn

\[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-Mz5G1IEpBZ3wq0WDdRwlsPyKnz2FXwUx2Q5fkdnY6AA\_AbQPFwl\_HHzoewZSXtuQFAGTzCcZRXzvDFmx2ERikLdcL8vhZhQDZPLYVaeF-Y6ukX5QpCrfuloT3f1NaNamLOo4ba-HzlQDShDPG4V8tIY75pKrwOK3OZ981k5wfnM0Q8ASdSStKGbwC3\_y/s1209/Screenshot%202024-10-04%20160035.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-Mz5G1IEpBZ3wq0WDdRwlsPyKnz2FXwUx2Q5fkdnY6AA_AbQPFwl_HHzoewZSXtuQFAGTzCcZRXzvDFmx2ERikLdcL8vhZhQDZPLYVaeF-Y6ukX5QpCrfuloT3f1NaNamLOo4ba-HzlQDShDPG4V8tIY75pKrwOK3OZ981k5wfnM0Q8ASdSStKGbwC3_y/s1209/Screenshot%202024-10-04%20160035.png))

Lời kết Vậy là với một vài bước đơn giản, chúng ta đã có thể import câu hỏi từ file docx/pdf vào anki một cách nhanh chóng mà không phải copy từng câu một. Có thể nó không được nhanh như bạn mong đợi, nhưng tin mình đi, thời gian bạn bỏ ra trong suốt quá trình này không hề vô ích chút nào đâu.

Nếu bạn muốn góp ý hoặc bổ sung thêm gì vào bài viết của mình, hay có đoạn nào chưa rõ, hãy đừng ngần ngại để lại một bình luận hoặc liên hệ trực tiếp để góp ý với mình nhé. Còn nếu thấy hay và bổ ích, hãy chia sẻ cho bạn của mình cùng biết. Chúc các bạn học tốt!

---

Góc quảng cáo Anki là một công cụ tuyệt vời, nó đã góp một phần không nhỏ vào kết quả tốt của mình trong kỳ thi Bác sĩ Nội trú vừa rồi. Sau khi thi xong mình muốn pass lại bộ anki mình đã sử dụng cho bạn nào có nhu cầu. Sơ qua về nội dung của bộ thẻ:

Gồm 8 môn học, mỗi môn gồm vài bộ đề cương trọng tâm nhất mà mình đã chắt lọc và rút kinh nghiệm qua cuộc thi Tất cả bộ thẻ mình đã đều học qua và check lại đáp án để giảm thiểu sai sót xuống mức thấp nhất, đồng thời nhiều bộ thẻ mình đã note thêm thông tin để học hiệu quả hơn \[

\]([https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2U\_BU4a-kjZ73PCCOy1Ifu05pxwi6gZGVFmU0C07sdHBUjZQ9Jb6Eq2Tqr9rhJzEi2OyiRyRbBDhiTrIuuf9\_srlk4lkmoLtWFQOEeK1ZA-r-ZdKgt3oJD8eiAh4WF3ijeAJItu\_0EcylNb324FmOiS-9\_kVuIFhs1nE7hvZooxS2ZZd4YBic5HHn7CVm/s889/Screenshot%202024-09-19%20215833.png](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2U_BU4a-kjZ73PCCOy1Ifu05pxwi6gZGVFmU0C07sdHBUjZQ9Jb6Eq2Tqr9rhJzEi2OyiRyRbBDhiTrIuuf9_srlk4lkmoLtWFQOEeK1ZA-r-ZdKgt3oJD8eiAh4WF3ijeAJItu_0EcylNb324FmOiS-9_kVuIFhs1nE7hvZooxS2ZZd4YBic5HHn7CVm/s889/Screenshot%202024-09-19%20215833.png))

demo chiếc anki deck với hơn 11600 thẻ

Nếu bạn cần bộ thẻ này, hãy nhắn tin cho mình qua Messenger hoặc email tới địa chỉ [luuquangvu.yhn@gmail.com](https://55tm-github-io.pages.dev/docs/H%E1%BB%8CC/ANKI/).

Cuối cùng, chân thành cảm ơn các bạn đã quan tâm!

1:23:09 PM