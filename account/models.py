import os
from hashlib import sha1, md5

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다.
        """
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name=_('Nickname'),
        max_length=30,
        unique=True
    )

    about = models.TextField(
        verbose_name=_('About'),
        max_length=255,
        blank = True, null = True,
    )

    facebook_url = models.CharField(
        verbose_name=_('Facebook link'),
        max_length=255,
        blank=True, null=True,
    )

    twitter_url = models.CharField(
        verbose_name=_('Twitter link'),
        max_length=255,
        blank=True, null=True,
    )

    pinterest_url = models.CharField(
        verbose_name=_('Pinterest link'),
        max_length=255,
        blank=True, null=True,
    )

    instagram_url = models.CharField(
        verbose_name=_('Instagram link'),
        max_length=255,
        blank=True, null=True,
    )

    gogle_plus_url = models.CharField(
        verbose_name=_('Gogle plus link'),
        max_length=255,
        blank=True, null=True,
    )

    image = models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True, null=True)

    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )


    # 이 필드는 레거시 시스템 호환을 위해 추가할 수도 있다.
    salt = models.CharField(
        verbose_name=_('Salt'),
        max_length=10,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.nickname

    def get_image(self):
        return self.image

    def get_about(self):
        return self.about

    def get_facebook(self):
        return self.facebook_url

    def get_twitter(self):
        return self.twitter_url

    def get_pinterest(self):
        return self.pinterest_url

    def get_instagram(self):
        return self.instagram_url

    def get_google_plus(self):
        return self.gogle_plus_url

    def get_short_name(self):
        return self.nickname

    #비밀번호 설정 오버라이딩
    def set_password(self, raw_password):
        # Opencart의 salt 값은 9자리의 alphanumeric 문자열
        salt = md5(os.urandom(128)).hexdigest()[:9]

        # Opencart PHP 프로그램의 비밀번호 암호화 알고리즘
        hashed = sha1(
            (salt + sha1(
                (salt + sha1(
                    raw_password.encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()).encode('utf8')
        ).hexdigest()

        self.salt = salt
        self.password = hashed

    #비밀번호 변경시 체크 오버라이딩
    def check_password(self, raw_password):
        try:
            user = User.objects.get(email=self.email)

            hashed = sha1(
                (user.salt + sha1(
                    (user.salt + sha1(
                        raw_password.encode('utf8')
                    ).hexdigest()).encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()

            if user.password == hashed:
                return True
            else:
                return False

        except User.DoesNotExist:
            return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    get_full_name.short_description = _('Full name')