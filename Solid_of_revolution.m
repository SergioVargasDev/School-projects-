% f(x) = 3x [0, 3]
% f(x) = -0.02x^2 + 0.5x + 8 [3, 10]
% original curve
x = 0:0.1:3;
y = 3*x;
% rotate for 360 grad
alpha=-pi:0.1:pi+0.1;
% calculate two other coordinates
px1 = cos(alpha)'*y;
py1 = sin(alpha)'*y;
x = kron(ones(length(alpha),1),x);
% plot
surf(px1,py1,x)

hold on
x2 = 3:0.1:10;
y2 = -0.01530612245*x2.^2+0.5204081633*x2+7.576530612;
px2 = cos(alpha)'*y2;
py2 = sin(alpha)'*y2;
x2 = kron(ones(length(alpha),1),x2);
surf(px2,py2,x2)
hold off
