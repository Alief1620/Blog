from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)  #уникально в своей таблице (тру)
    heading = models.CharField(max_length=200, unique=True)  #уникально в своей таблице (тру)
    content = models.TextField('Content')
    updated_on = models.DateTimeField(auto_now=True)  #используют дату в часовом поясе в момент создания или обновления
    created_on = models.DateField('Date of publication')

    def __str__(self):
        return f' {self.title}'

    class Meta:
        verbose_name = 'Write'
        verbose_name_plural = 'Writes'


class User(models.Model):
    firstname = models.CharField('firstname', max_length=20)
    lastname = models.CharField('lastname', max_length=20)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.lastname}, {self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('text_comments', max_length=2000)
    post_id = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.user_id}, {self.post_id}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


