import wx

# 参考教程 https://www.codingdict.com/article/7716
# 创建对象
app = wx.App()
# 绘制窗体
window = wx.Frame(None, title ="wxPython Frame", size = (300, 200))
# 绘制布局
panel = wx.Panel(window)
# 绘制标签：内容
label = wx.StaticText(panel, label ="Hello World", pos = (100, 50))
# 显示内窗口
window.Show(True)
app.MainLoop()