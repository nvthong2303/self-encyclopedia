# Angular

## Angular là gì ?

- frameworks phát triển ứng dụng web mã nguồn mở, phổ biến, cộng đồng lớn, đc duy trì bởi google, sử dụng typescript.
- các thành phần, tính năng chính trong angular:
  - Components: các block cơ bản trong angular, có thể tái sử dụng.
    - Class (typescript): chứa logic của component
    - Template (HTML): định nghĩa giao diện của component
    - Styles (CSS): định nghĩa styles cho component
  - Module: là nơi tổ chức các thành phần của ứng dụng, mỗi ứng dụng có ít nhất 1 module chính (appModule), module giúp chia nhỏ các thành phần để dễ quản lý, đồng thời cung cấp các service, component và pipe cho các thành phần khác.
  - Templates: HTML được liên kết với một component, định nghĩa UI của component
  - Directives: phần mở rộng đê thay đổi hoặc thêm các action cho các phần tử trong template.
    - Structural directives: thay đổi cấu trúc của DOM (*ngIf, *ngFor)
    - Attribute directives: thay đổi hiện thị hoặc action của phần tử (ngClass, ngStyle)
  - Services: là class chứa logic, data, method cho component, thường sử dụng để call api hoặc xử lý các login không ảnh hưởng trực tiếp đến UI
  - Dependency Injection: DI cho phép Angular quản lý các dependencies giữa các thành phần. Giúp các thành phần không cần tạo các service mà có thể tái sử dụng thông qua DI.
  - Routing: sử dụng RouterModule định tuyến điều hướng đến các component khác nhau.
  - Pipes: công cụ biến đổi dữ liệu trong template, có thể customPipe
  - Forms: Angular hỗ trợ 2 loại: Template-driven forms: sử dụng html để tạo và quản lý form. Reactive forms: cung cấp nhiều quyền kiểm soát form thông qua typescript.
  - Lifecyle Hooks: Angular cung cấp các phương thức ngOnInit(), ngOnChanges(), ngOnDestroy(), ...
  - HTTPClient: service trong Angular dùng gửi các http request và nhận response.
  - Binding data:
    - Interpolation: {{ variable }} -> dùng để hiển thị giá trị biến trong template
    - Property Binding: [property]="value" -> binding data từ component sang thuộc tính của element
    - Event Binding: (event)="onChange()" -> lắng nghe và xử lý sự kiện từ element
    - Two-way Binding: [(ngModel)]="variable" -> kết hợp cả property bind và event binding.ví dụ
  - RxJS:
