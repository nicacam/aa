# V2Board AutoSub

本仓库通过GitHub Actions自动于指定V2Board站点注册账户并获取试用订阅。

## 使用本仓库抓取的订阅

订阅每小时更新： https://raw.githubusercontent.com/arielherself/autosub/main/subs.txt

请注意，这个链接**不是一个订阅链接**，而是多个订阅链接的集合。请用浏览器打开，然后复制里面的订阅链接。

*受资源配额影响，在GitHub Actions设置的定时任务不一定会准时执行。*

## 手动抓取订阅

开始之前请确保目标站点满足以下条件：

- 使用V2Board面板
- 注册时不需要邮箱验证码
- 未设有DDoS防御机制

对于最后一点，可以通过手动注册一个账户，然后获取订阅链接的前半部分来规避。首先Fork本仓库，然后修改`autosub_v2b.py`文件中`home_url`中的值为目标站点的URL。为了获得推送权限，还需要在GitHub设置的"Developer Settings">"Personal Access Token"中添加名为"GITHUB_TOKEN"的令牌并授予仓库读写及Workflow权限。

`home_url`正确格式示例：

```
https://example.com
http://example.com
```

错误格式示例：

```
example.com
https://example.com/
https://example.com/#/register
```
