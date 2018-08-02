from qiniu import Auth, put_file, etag
import sys
print('参数个数为:', len(sys.argv), '个参数。')
print('参数列表:', str(sys.argv))

# backUpFolder
backUpFolder = sys.argv[1]
# backUpFileName
backUpFileName = sys.argv[2]
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'your_key'
secret_key = 'your_key'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'test'
# 上传到七牛后保存的文件名
key = backUpFileName
# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
# 要上传文件的本地路径
localfile = backUpFolder + backUpFileName
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
