import m_docstr

print(m_docstr.__doc__)
print(m_docstr.func.__doc__)
print(m_docstr.spam.__doc__)
m_docstr.spam.method.__doc__
x = m_docstr.spam()
x.method()

